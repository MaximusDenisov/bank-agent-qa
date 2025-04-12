from pathlib import Path

# Определение корневого пути проекта
root_dir = Path(__file__).resolve().parent.parent  # simple/


def get_external_files_path(subdir: str = "") -> str:
    """Возвращает путь к каталогу проекта с возможным подкаталогом."""
    path = root_dir / "external_project" / subdir
    if not path.exists():
        raise FileNotFoundError(f"Путь не найден: {path}")
    return str(path)


def get_output_dir(subdir: str = "") -> str:
    """Возвращает путь к директории для автогенерированных тестов."""
    path = root_dir / "external_project" / subdir / "generated_tests"
    path.mkdir(parents=True, exist_ok=True)  # гарантирует, что путь существует
    return str(path)