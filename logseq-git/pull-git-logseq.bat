@echo off
cd C:\Users\jwolf\Documents\logseq
git checkout main
git pull
git checkout desktop
git merge main
@pause