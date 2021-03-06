rm *md *jpg *png *py
cp ../documentation/*png .

cp ../intro/* .
cp ../traffic/* .
cp ../teleport/* .
cp ../trap/* .
cp ../photobooth/* .
cp ../big_buildings/* .
cp ../pixel_art/* .
cp ../treasure/* .

echo '% Python and Minecraft' > handout.md
echo '% CPD for Teachers' >> handout.md
echo '% ' >> handout.md

for file in intro traffic teleport trap photobooth big_buildings pixel_art treasure; do
    echo $file
    echo -e '\\newpage\n' >> handout.md
    cat $file.md  >> handout.md
done
