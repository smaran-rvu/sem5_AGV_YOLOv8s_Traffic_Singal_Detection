cd ./train/images
mv *.* ../
cd ..

cd ./train/labels
mv *.* ../
cd ..

rm images labels -r
cd..

cd ./test/images
mv *.* ../
cd ..

cd ./test/labels
mv *.* ../
cd ..

rm images labels -r
cd ..

cd ./valid/images
mv *.* ../
cd ..

cd ./valid/labels
mv *.* ../
cd ..

rm images labels -r
cd ..