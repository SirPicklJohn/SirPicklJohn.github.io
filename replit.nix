{ pkgs }: {
  deps = [
    pkgs.cowsay
    pkgs.python39Full
    pkgs.qtile
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}