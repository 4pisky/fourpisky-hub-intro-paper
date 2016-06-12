project (version-controlled-paper)
cmake_minimum_required (VERSION 2.8)

set ( MANUSCRIPT_NAME fourpisky_hub_intro )

set (CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
set (FIGURE_OUTPUT_DIR ${PROJECT_BINARY_DIR}/figures)

find_package (LATEX REQUIRED)
find_package (LatexMk REQUIRED)
find_package (PythonInterp REQUIRED)

# Versioning
execute_process (
    COMMAND git log -1 --date=short --pretty=\\newcommand{\\githash}{%h}\\newcommand{\\gitdate}{%ad}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    OUTPUT_VARIABLE GIT_CMD
)


# We copy all the static figures from the source tree to a 'figures' folder 
# under the build root.
file(GLOB STATIC_FIGURES
    "${PROJECT_SOURCE_DIR}/figures/*.pdf"
)

foreach (figure ${STATIC_FIGURES})
    get_filename_component(figure_basename ${figure} NAME)
    MESSAGE( STATUS "Copying figure:  " ${figure_basename} )
    configure_file (
        ${figure}
        ${PROJECT_BINARY_DIR}/figures/${figure_basename}
        COPYONLY
    )
endforeach (figure)

# Likewise we copy all files from the 'manuscripts' folder to the build root
file(GLOB MANUSCRIPT_FILES
    "${PROJECT_SOURCE_DIR}/manuscript/*"
)

foreach (manuscript ${MANUSCRIPT_FILES})
    get_filename_component(manuscript_basename ${manuscript} NAME)
    MESSAGE( STATUS "Copying manuscript:  " ${manuscript_basename} )
    configure_file (
        ${manuscript}
        ${PROJECT_BINARY_DIR}/${manuscript_basename}
        @ONLY
    )
endforeach (manuscript)


add_custom_command (
    OUTPUT ${PROJECT_BINARY_DIR}/${MANUSCRIPT_NAME}.pdf
    COMMAND ${LATEXMK_EXECUTABLE}
    ARGS -pdf -pdflatex=\"pdflatex --shell-escape %O %S\" ${PROJECT_BINARY_DIR}/${MANUSCRIPT_NAME}.tex
    DEPENDS
        ${PROJECT_BINARY_DIR}/${MANUSCRIPT_NAME}.tex
        ${PROJECT_BINARY_DIR}/${MANUSCRIPT_NAME}.bib
#  #List of generated figures we also depend on:
#  ${FIGURE_OUTPUT_DIR}/results/V_predictedVobserved.pdf
)

add_custom_target (paper ALL echo
    DEPENDS ${PROJECT_BINARY_DIR}/${MANUSCRIPT_NAME}.pdf
)
