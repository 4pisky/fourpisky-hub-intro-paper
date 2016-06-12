MANUSCRIPT_NAME=fourpisky_hub_intro

for FILESUFFIX in aux bib blg fdb_latexmk fls log out pdf spl; do
    rm -fv build/${MANUSCRIPT_NAME}.${FILESUFFIX}
done

rm -rfv build/CMake*
rm -fv build/cmake*
rm -fv build/Makefile

tar zc build > ${MANUSCRIPT_NAME}_arxiv_upload.tar.gz
