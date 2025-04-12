"""Главный модуль для взаимодействия с агентом GigaChat."""

# Импорты
from src.agent import generate_tests_for_project
from src.utils import get_external_files_path, root_dir, get_output_dir


if __name__ == "__main__":
    generate_tests_for_project(
        project_path=get_external_files_path("coffee-autotests"),
        analysis_file=root_dir / "external_cases" / "analysis.txt",
        output_dir=get_output_dir(get_external_files_path("coffee-autotests"))
    )