exec { 'fix_typo':
  command => "sed -i 's/phpp/php/'"
}