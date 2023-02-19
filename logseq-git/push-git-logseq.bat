@echo off
cd C:\Users\user\Documents\My Documents\logseq
git checkout desktop
git add -A
git commit -m "auto-script commit"
git push -v origin desktop:desktop
git checkout main
git merge desktop
git push -v origin main:main
git checkout desktop
@pause