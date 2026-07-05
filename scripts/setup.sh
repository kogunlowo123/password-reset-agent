#!/bin/bash
set -euo pipefail
echo "Setting up Password Reset Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
