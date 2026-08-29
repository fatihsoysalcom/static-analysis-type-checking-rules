# Static Analysis Type Checking Rules

This example demonstrates how static analysis tools, particularly type checkers like `mypy`, enforce explicit code specifications (type hints) to catch potential bugs before runtime. It illustrates cases where static analysis successfully identifies type mismatches and `None` values, preventing common errors. The example also highlights limitations, showing how basic static analysis might miss violations of implicit business rules or value range assumptions, which would instead trigger runtime errors.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run the script: `python main.py`
3. To see static analysis in action, install `mypy` (`pip install mypy`) and run: `mypy main.py`

## Original Article

This example accompanies the Turkish article: [Statik Analiz Kuralları: Spesifikasyondan Doğru Bir Varsayım mı?](https://fatihsoysal.com/blog/statik-analiz-kurallari-spesifikasyondan-dogru-bir-varsayim-mi/).

## License

MIT — see [LICENSE](LICENSE).
