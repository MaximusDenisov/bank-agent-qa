import os


def read_project_files(directory: str, extensions: list = [".java"]):
    project_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    project_data.append((path, content))
    return project_data


def build_prompt_from_project(project_files):
    prompt_parts = ["Ниже представлен проект автотестов на Java (TestNG)."]
    for path, content in project_files:
        prompt_parts.append(f"\nФайл: {path}\n```\n{content}\n```")
    prompt_parts.append(
        "\nПроанализируй проект. Предложи улучшения архитектуры, покрытия, структуры. "
        "Затем предложи как минимум один дополнительный автотест, который стоит реализовать, "
        "и сгенерируй его код на Java (TestNG)."
    )
    return "\n".join(prompt_parts)