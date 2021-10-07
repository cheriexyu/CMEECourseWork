##!/bin/bash
echo "Cherie is pretty and cute!!!" | tr "[:lower:]" "[:upper:]"
#Make sure between [] are quotation marks

echo "Cats only have four legs" | tr -d "f"

echo "Horses      are       amazing" | tr -s " "

echo "10.00 only numbers 1.55" | tr -d '[:alpha:]' | tr -s " " ","

#exit