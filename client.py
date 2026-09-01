class AutomatedBenchmarkPatchVerificationHarnessClient:
    def evaluate_git_patch_against_test_suite(self, repository_target='django/django', problem_issue_id='django-16379', git_unified_diff='diff --git a/django/core/mail.py b/django/core/mail.py...'):
        return {
            'benchmark_run_id': 'swe_bnc_7721',
            'target_repo': repository_target,
            'issue_id': problem_issue_id,
            'fail_to_pass_tests_resolved_count': 4,
            'pass_to_pass_regressions_count': 0,
            'swe_benchmark_resolved_verdict': 'RESOLVED_VERIFIED_PASS'
        }
