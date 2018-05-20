SELECT
  FirstName,
  LastName,
  City,
  State
FROM Person p
  Left JOIN Address a ON a.PersonId = p.PersonId