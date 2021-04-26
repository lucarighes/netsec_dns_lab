#!/bin/bash

#clean cache
rndc flush
rndc reload

echo "The cache is clean now!" 
