@echo off
echo �z�z���ꂽDjango�̉��z���̃Z�b�g�A�b�v���J�n���܂��B

REM ���z�����쐬
python -m venv ll_env

REM ���z����L����
call ll_env\Scripts\activate

REM �ˑ��p�b�P�[�W���C���X�g�[��
pip install -r requirements.txt

REM ------------------------------------------------------------------
REM ���f���ύX�����o���ă}�C�O���[�V�����t�@�C�����쐬
echo.
echo ���f���ύX�����o���ă}�C�O���[�V�����t�@�C�����쐬���܂�...
python manage.py makemigrations

REM �f�[�^�x�[�X�Ƀ}�C�O���[�V������K�p
echo.
echo �f�[�^�x�[�X�Ƀ}�C�O���[�V������K�p���܂�...
python manage.py migrate
REM ------------------------------------------------------------------

REM �I�����b�Z�[�W
echo.
echo ���z���̃Z�b�g�A�b�v�Ə����}�C�O���[�V�������������܂����B
pause