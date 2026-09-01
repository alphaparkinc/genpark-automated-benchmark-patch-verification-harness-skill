from client import AutomatedBenchmarkPatchVerificationHarnessClient

def main():
    client = AutomatedBenchmarkPatchVerificationHarnessClient()
    res = client.evaluate_git_patch_against_test_suite('pallets/flask', 'flask-5014')
    print('SWE Benchmark Harness: ' + res['benchmark_run_id'] + ' (' + res['target_repo'] + ')')
    print('Resolved Tests: ' + str(res['fail_to_pass_tests_resolved_count']) + ' | Regressions: ' + str(res['pass_to_pass_regressions_count']))
    print('Verdict: ' + res['swe_benchmark_resolved_verdict'])

if __name__ == '__main__':
    main()
