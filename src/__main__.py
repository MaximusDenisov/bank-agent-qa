"""Главный модуль для взаимодействия с агентом GigaChat."""

# Импорты
from src.agent import generate_tests_for_project, load_csv_prompts
from src.utils import get_external_files_path, root_dir, get_output_dir, get_external_cases_csv_files_path

if __name__ == "__main__":
    some_csv_docs = load_csv_prompts(get_external_cases_csv_files_path())
    for doc in some_csv_docs:
        print(doc.page_content)
    generate_tests_for_project(
        project_path=get_external_files_path("coffee-autotests"),
        csv_directory=get_external_cases_csv_files_path(),
        output_dir=get_output_dir(get_external_files_path("coffee-autotests"))
    )