# Порівняння реалізацій обчислення визначника матриці

## Опис проекту

Проект містить реалізації обчислення визначника матриці 4x4 з випадковими значеннями (1-9) на мовах Python та Julia. Обидві реалізації використовують однаковий алгоритм з урахуванням особливостей кожної мови.

## Структура проекту

- `matrix_determinant_python.py` - реалізація на Python
- `matrix_determinant_julia.jl` - реалізація на Julia
- `requirements.txt` - залежності для Python
- `REPORT.md` - звіт з аналізом та порівнянням

## Вимоги

### Python
- Python 3.7+
- NumPy (встановити через `pip install -r requirements.txt`)

### Julia
- Julia 1.6+

## Запуск

### Python
```bash
python matrix_determinant_python.py
```

### Julia
```bash
julia matrix_determinant_julia.jl
```

## Алгоритм

Обидві реалізації використовують стандартні бібліотеки для обчислення визначника:
- **Python**: `numpy.linalg.det()` - використовує LU-розклад
- **Julia**: `LinearAlgebra.det()` - використовує LU-розклад

## Вимірювання продуктивності

- **Час виконання**: вимірюється в мілісекундах
- **Пам'ять**: вимірюється в кілобайтах
  - Python: використовує `tracemalloc`
  - Julia: використовує макрос `@allocated`

