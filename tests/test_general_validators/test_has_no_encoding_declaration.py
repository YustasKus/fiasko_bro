from fiasko_bro import defaults
from fiasko_bro.validators import has_no_encoding_declaration


def test_has_no_encoding_declarations_paths_to_ignore_fails(origin_repo):
    expected_output = 'has_encoding_declarations_paths_to_ignore', 'file_with_encoding_declarations.py'
    ignore_list = defaults.VALIDATION_PARAMETERS['encoding_declarations_paths_to_ignore']
    output = has_no_encoding_declaration(
        project_folder=origin_repo,
        encoding_declarations_paths_to_ignore=ignore_list
    )
    assert output == expected_output


def test_has_no_encoding_declarations_paths_to_ignore_succeeds(test_repo):
    ignore_list = defaults.VALIDATION_PARAMETERS['encoding_declarations_paths_to_ignore']
    output = has_no_encoding_declaration(
        project_folder=test_repo,
        encoding_declarations_paths_to_ignore=ignore_list
    )
    assert output is None

