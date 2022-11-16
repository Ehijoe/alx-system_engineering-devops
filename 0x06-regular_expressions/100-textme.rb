#!/usr/bin/env ruby

LOG = /\[from:?(?<from>(\w*)|(\+?\d*))\] \[to:?(?<to>(\w*)|(\+?\d*))\] \[flags:(?<flags>(-?[01]:){4}(-?[01]))\]/

for line in ARGV[0].split("\n") do
  m = line.match(LOG)
  if m
    puts '%s,%s,%s' %[m.named_captures["from"], m.named_captures["to"], m.named_captures["flags"]]
  end
end
