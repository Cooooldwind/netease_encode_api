del dist /Q /F
python -m build
twine upload dist/*
del dist /Q /F
pause