@echo off
echo �N���[���A�b�v���J�n���܂�...

:: 1. ���z���t�H���_�ill_env�j���폜
echo.
echo ���z���t�H���_ (ll_env) ���폜��...
if exist "ll_env" (
    rmdir /s /q "ll_env"
    timeout /t 2 >nul
    if not exist "ll_env" (
        echo �폜����: ll_env
    ) else (
        echo ?? �폜�Ɏ��s�������A�t�@�C�����g�p���ł�: ll_env
    )
) else (
    echo �t�H���_��������܂���: ll_env
)

:: 2. Python�L���b�V���t�H���_�i__pycache__�j���ꊇ�폜
echo.
echo Python�L���b�V���t�H���_ (__pycache__) �������E�폜��...
set "deleted_cache=0"
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        rmdir /s /q "%%d"
        echo �폜����: %%d
        set "deleted_cache=1"
    )
)
if "%deleted_cache%"=="0" (
    echo __pycache__ �t�H���_�͌�����܂���ł����B
)

echo.
echo �N���[���A�b�v���������܂����B
pauses