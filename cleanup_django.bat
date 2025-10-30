@echo off
echo クリーンアップを開始します...

:: 1. 仮想環境フォルダ（ll_env）を削除
echo.
echo 仮想環境フォルダ (ll_env) を削除中...
if exist "ll_env" (
    rmdir /s /q "ll_env"
    timeout /t 2 >nul
    if not exist "ll_env" (
        echo 削除完了: ll_env
    ) else (
        echo ?? 削除に失敗したか、ファイルが使用中です: ll_env
    )
) else (
    echo フォルダが見つかりません: ll_env
)

:: 2. Pythonキャッシュフォルダ（__pycache__）を一括削除
echo.
echo Pythonキャッシュフォルダ (__pycache__) を検索・削除中...
set "deleted_cache=0"
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        rmdir /s /q "%%d"
        echo 削除完了: %%d
        set "deleted_cache=1"
    )
)
if "%deleted_cache%"=="0" (
    echo __pycache__ フォルダは見つかりませんでした。
)

echo.
echo クリーンアップが完了しました。
pauses