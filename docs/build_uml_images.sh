#!/bin/sh

rm -rf images/generated/*
plantuml -o ../images/generated graphics/*.uml
