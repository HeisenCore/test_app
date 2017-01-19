#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault('HEISEN_SETTINGS_MODULE', 'config.settings')

    from heisen.cli import main

    main()

