While install "pip install crewai"
it show an error which is give below:

Building wheel for chroma-hnswlib (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for chroma-hnswlib (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [5 lines of output]
      running bdist_wheel
      running build
      running build_ext
      building 'hnswlib' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/   
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for chroma-hnswlib
Failed to build chroma-hnswlib
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (chroma-hnswlib)

SOLUTION:


To Resolve this issue in Windows

You need to download https://visualstudio.microsoft.com/visual-cpp-build-tools/ first.

Next, navigate to "Individual components", find these two
MCVS v143 VS2022 C++ x64/86 latest

and Windows 10 SDK
Windows 11 SDK latest👍👍
