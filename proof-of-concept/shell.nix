{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages(ps: with ps; [ paho-mqtt pyserial pydantic python-lsp-server]);

in
pkgs.mkShell {
  packages = with pkgs; [
    arduino-cli
    arduino
    pythonEnv
    black
  ];
}

