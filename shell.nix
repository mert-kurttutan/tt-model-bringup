{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  buildInputs = [
    pkgs.pkg-config
  ];

  shellHook = ''
    # you need cuda installed for the following to work in your system
    export LD_LIBRARY_PATH=/run/opengl-driver/lib:$LD_LIBRARY_PATH
  '';
}
