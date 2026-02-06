jq -n \
  --arg system "$SYSTEM" \
  --arg owner "$OWNER" \
  --arg owner_name "$OWNER_NAME" \
  --arg owner_contact "VERIFIED" \
  --arg version "$VERSION" \
  --arg type "$TYPE" \
  --arg title "$TITLE" \
  --arg body "$BODY" \
  --arg url "$URL" \
  --arg author "$AUTHOR" \
  --arg ts "$(date -u +%FT%TZ)" \
  '{
    system,
    owner,
    owner_name,
    owner_contact,
    version,
    type,
    title,
    body,
    url,
    author,
    timestamp: $ts
  }' > payload.json
