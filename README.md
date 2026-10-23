# practica-pruebas-software

Proyecto educativo para aplicar técnicas de pruebas de software con **Python**, **pytest**, **GitHub Issues**, **Pull Requests** y **GitHub Actions (CI)**.

## Alumno
- **Jorge Alonso Romo de Vivar Rosas** — `5123180040`

## Estructura del Proyecto
- `calculadora.py`: Módulo principal con las funciones `sumar`, `restar`, `multiplicar` y `dividir` (incluye validación contra división entre cero y validación de entradas no numéricas).
- `test_calculadora.py`: Suite de pruebas unitarias automatizadas con `pytest` (casos iniciales `CP01`–`CP05` + actividad complementaria `CP06`–`CP13`).
- `.github/workflows/pruebas.yml`: Flujo de integración continua en GitHub Actions que ejecuta `python -m pytest -v` en cada `push` y `pull_request`.

## Ejecución de las Pruebas
```bash
python -m pip install pytest
python -m pytest -v
```
