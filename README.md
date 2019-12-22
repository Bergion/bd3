# bd3
Variant 3 \
Vintsyk D.

## Task 2
Hash index:\
CREATE INDEX blog_id_idx on social_network_post \
USING HASH(blog_id);

GIN index:\
CREATE INDEX content_idx on t \
USING GIN(content_tsv);
