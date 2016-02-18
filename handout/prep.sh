rm *md *jpg *png
cp ../documentation/*png .

cp ../intro/* .
cp ../traffic_lights/* .
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
    cat $file.md  >> handout.md
    echo -e '\\newpage\n' >> handout.md
done
