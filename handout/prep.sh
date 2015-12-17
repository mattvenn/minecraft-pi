rm *md *jpg *png
cp ../documentation/*png .

cp ../trap/* .
cp ../photobooth/* .
cp ../big_buildings/* .
cp ../traffic_lights/* .
cp ../pixel_art/* .
cp ../teleport/* .
cp ../treasure/* .

echo '% Python and Minecraft' > handout.md
echo '% CPD for Teachers' >> handout.md
echo '% ' >> handout.md

cat big_buildings.md  >> handout.md
echo -e '\\newpage\n' >> handout.md

cat traffic.md  >> handout.md
echo -e '\\newpage\n' >> handout.md

cat trap.md >> handout.md
echo -e '\\newpage\n' >> handout.md

cat photobooth.md >> handout.md
echo -e '\\newpage\n' >> handout.md

cat pixel_art.md  >> handout.md
echo -e '\\newpage\n' >> handout.md

cat teleport.md  >> handout.md
echo -e '\\newpage\n' >> handout.md

cat treasure.md >> handout.md
