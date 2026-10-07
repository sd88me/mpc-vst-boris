#!/usr/bin/env bash
# Build Boris Granular as an MPC OS VST2 effect: skin, params.h, .so and plugin-list entry in vst/build/.
# Needs a checkout of https://github.com/sd88me/mpc-vst-plugins: $MPC_VST, default ../mpc-vst-plugins.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
MPC_VST="${MPC_VST:-$here/../mpc-vst-plugins}"
exec "$MPC_VST/tools/build_port.sh" "$here/vst/vst.json"
