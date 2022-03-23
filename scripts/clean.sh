autoflake \
    --in-place \
    --recursive \
    --expand-star-imports \
    --remove-all-unused-imports \
    --remove-duplicate-keys \
    modules/ \
    main.py
