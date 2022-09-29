#!/usr/bin/env bash

jq . food.json | sponge food.json
