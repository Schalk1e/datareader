from datareader.helpers import _build_df_dict


def test_build_df_dict(test_build_df_dict_cases):
    for case in test_build_df_dict_cases:
        assert (
            _build_df_dict(case.input_value[0], case.input_value[1])
            == case.output_value
        )
