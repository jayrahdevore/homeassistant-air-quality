{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages(ps: with ps; [ ]);

in
pkgs.mkShell {
  packages = with pkgs; [
    pythonEnv
    screen
    black
    adafruit-ampy
    mosquitto

  ];
}

