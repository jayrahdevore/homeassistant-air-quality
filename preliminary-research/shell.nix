{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages(ps: with ps; [ paho-mqtt ]);

in
pkgs.mkShell {
  packages = with pkgs; [
    arduino-cli
    arduino
    pythonEnv
    black
  ];
}

