module.exports = function namedSchemaRequired(targetVal) {
  const reserved = ['type','properties','required','description','title','allOf','anyOf','oneOf','items','enum'];
  const keys = Object.keys(targetVal || {});
  const isInvalid = keys.every(k => reserved.includes(k));
  return isInvalid
    ? [
        {
          message: `Schema must define a named object key — only keywords found: ${keys.join(", ")}`
        }
      ]
    : [];
};
