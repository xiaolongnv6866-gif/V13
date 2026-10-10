#!/usr/bin/env python3
"""B068 authentic paired-output and scoring structure audit; not an independent literary verdict."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_SHA = '4e24d782632210c1e1637eba4954bde3d8f3846f'
R68 = ['WM-f01', 'WM-f02', 'WM-f04', 'WM-f06', 'WM-f08', 'WM-f10', 'WM-f12']
R69_FIRST = ['WM-f13', 'WM-f14', 'WM-p01', 'WM-p03']
EXPECTED = R68 + R69_FIRST


def check(b, message):
    if not b:
        raise AssertionError(message)


def load_json(path):
    return json.loads((ROOT/path).read_text('utf-8'))


def load_tsv(path):
    with (ROOT/path).open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def han(text):
    return len(re.findall(r'[\u3400-\u9fff]', text))


frozen = load_json('v2/v3/FROZEN_TEST_CONTRACT.json')
tests = {x['candidate_id']: x for x in frozen['cases']}
allocation = {x['candidate_id']: x for x in load_tsv('v2/v3/V3_TASK_ALLOCATIONS.tsv')}
state = load_json('V13_CURRENT_V3.json')
check(len(EXPECTED) == len(set(EXPECTED)) == 11, 'eleven exact candidates')
check(state['v3_original_47_completed'] in (0, 11, 21, 30, 39, 47), 'valid aggregated testing cursor')
check(state['skill_certified_count'] == 0 or state['current_batch'] not in ('B068','B069'), 'no early certification')
rows = load_tsv('v2/v3/results/R68_WM_7.tsv') + load_tsv('v2/v3/results/R69_WM_4_PARTIAL.tsv')
check(len(rows) == 11 and set(x['candidate_id'] for x in rows) == set(EXPECTED), 'exactly eleven unique result rows')

for row in rows:
    ident = row['candidate_id']
    source = tests[ident]
    check(source['allocated_batch'] == 'B068', ident + ' must be assigned to B068')
    check(source['test_id'] == row['test_id'], ident + ' frozen test_id')
    check(source['legacy_round'] == row['legacy_round'], ident + ' original round')
    check(all(x['id'] == f'S{i}' for i,x in enumerate(source['scoring']['shared_rubric'],start=1)), ident + ' frozen S1-S5')
    path = Path(row['raw_output_path'])
    check(str(path) == f'outputs/{"R68" if ident in R68 else "R69"}/{ident}.json', ident + ' result path')
    data = load_json('v2/v3/' + str(path))
    check(data['test_id'] == source['test_id'] and data['candidate_id'] == ident, ident + ' raw test identifier')
    check(data['frozen_contract_blob_sha1'] == CONTRACT_SHA, ident + ' unchanged frozen contract')
    check(data['experiment_mode'] == 'DIAGNOSTIC_ONLY_NONBLIND', ident + ' nonblind label')
    check(data['independent_judge'] == 'NOT_AVAILABLE' and data['skill_verified'] is False, ident + ' no fabricated independence')
    check(data['arm_parity_contract'] and data['environment_note'], ident + ' parity and contamination disclosure')
    for arm in ('baseline', 'method'):
        s = data[arm]
        check(all(isinstance(s[k],str) and s[k].strip() for k in ('scene_one','scene_two','failure_risk_note')), ident + f' {arm} both scenes')
        actual = han(s['scene_one'] + s['scene_two'])
        check(500 <= actual <= 750, ident + f' {arm} 500-750 Han actual')
        check(actual == int(s['chinese_characters']) == int(row[arm + '_chars']), ident + f' {arm} actual count')
        check(len(s['state_ledger']) >= 4 and len(s['unknowns']) >= 1, ident + f' {arm} state and unknowns')
        check(all(isinstance(q,dict) and q.get('fact') for q in s['state_ledger']), ident + f' {arm} state entries')
        components = [int(t) for t in row[arm + '_scores'].split('/')]
        check(len(components) == 5 and all(0 <= x <= 2 for x in components), ident + f' {arm} S1-S5 0-2')
        check(sum(components) == int(row[arm + '_total']), ident + f' {arm} score arithmetic')
    delta = int(row['method_total']) - int(row['baseline_total'])
    check(delta == int(row['delta']), ident + ' accurate delta')
    check(row['skill_verified'] == 'NO' and row['evaluation_mode'] == 'DIAGNOSTIC_ONLY_NONBLIND', ident + ' diagnosis only')
    check(row['observed_failure_or_limit'] and row['hypothetical_counterexample_risk'], ident + ' failure and counterexample')
    check(row['baseline_evidence_quote'] and row['method_evidence_quote'], ident + ' evidence quote')
    # This is a structural validator; quoted excerpts and literary judgments are not independent certifications.
    task = allocation[ident]
    check(task['v3_execution_batch'] == 'B068' and task['legacy_round'] == row['legacy_round'], ident + ' allocation')
    if state['v3_original_47_completed'] >= 11:
        check(task['baseline_arm_status'] == 'TESTED_NONBLIND' and task['method_arm_status'] == 'TESTED_NONBLIND', ident + ' marked tested')
        check(task['v3_status'] == 'TESTED_NONBLIND_NO_DEMONSTRATED_GAIN' and task['certified'] == 'NO', ident + ' not certified')
    else:
        check(task['v3_status'] in ('NOT_TESTED','TESTED_NONBLIND_NO_DEMONSTRATED_GAIN'), ident + ' staged allowed')

check(set(x['candidate_id'] for x in load_tsv('v2/v3/results/R68_WM_7.tsv')) == set(R68), 'original R068 7/7')
check(set(x['candidate_id'] for x in load_tsv('v2/v3/results/R69_WM_4_PARTIAL.tsv')) == set(R69_FIRST), 'old R069 only 4/7 staged')
if state['v3_original_47_completed'] == 11:
    check(state['last_passed_batch'] == 'B068' and state['current_batch'] == 'B069', 'B068 sealed, next B069')
print('B068 STRUCTURE PASS: 11/11 IDs, 22 actual matched scene pairs, 7+4, 500-750 Han, states, five scored dimensions, 0 certified; only structural and self-rated evidence')
