# Python2
git add README.md

git config --global user.name "Hyuki56"
git config --global user.email "soundaim56@gmail.com"
git config --global --list # 깃 사용자 리스트 확인

git commit -m "커밋 내용"

git branch -M main # master → main으로 이름 변경, 자동으로 main으로 이동
git branch # 생성된 브랜치 확인

git init → 현재 폴더를 Git 저장소로 만듦
git add . → 모든 파일 스테이징

git remote add origin https://github.com/Hyuki56/Python2.git
git remote -v

git push -u origin main
