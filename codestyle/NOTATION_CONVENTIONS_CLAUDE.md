# Notation Conventions in arend-lib

This document describes the notational and stylistic conventions observed in the `src/` directory of [JetBrains/arend-lib](https://github.com/JetBrains/arend-lib). Every rule stated here is inferred from repeated patterns across multiple source files.

---

## Table of Contents

1. [Naming Conventions](#1-naming-conventions)
2. [Structural Conventions](#2-structural-conventions)
3. [Mathematical Notation Style](#3-mathematical-notation-style)
4. [Definitions and Proof Patterns](#4-definitions-and-proof-patterns)
5. [Argument and Type Conventions](#5-argument-and-type-conventions)
6. [Documentation and Comment Style](#6-documentation-and-comment-style)
7. [Formatting and Layout Conventions](#7-formatting-and-layout-conventions)
8. [Consistency Rules](#8-consistency-rules)
9. [Observed Style Guide (Inferred)](#9-observed-style-guide-inferred)

---

## 1. Naming Conventions

### 1.1 PascalCase — Types, Classes, Records, Modules

PascalCase is used consistently for:

- **Class definitions**: `Monoid`, `Semigroup`, `Group`, `CancelMonoid`, `PseudoRing`, `MeetSemilattice`
- **Record definitions**: `MonoidHom`, `AddMonoidHom`, `SemiringHom`, `RingHom`, `GCD`, `LIdeal`, `RIdeal`
- **`\data` types**: `List`, `Poly`, `Preorder`, `Poset`
- **Module names** (in `\module ... \where`): `NatOrder`, `TwoOutOfThree`, `Transports`, `Sort`, `Insertion`, `RedBlack`
- **Top-level file names mirror PascalCase**: `Monoid.ard`, `Group.ard`, `Ring.ard`, `PartialOrder.ard`

### 1.2 camelCase — Functions, Lemmas, Proofs, Fields

camelCase is the dominant style for:

- **`\func` definitions**: `arrayExt`, `headDef`, `mkArray`, `ipow`, `BigProd`, `length_map`
- **`\lemma` names**: `pow_+`, `ide-left`, `inverse-left`, `func-BigSum`, `contains_pow`
- **Record fields**: `func-*`, `func-ide`, `func-+`, `inverse-right`, `ideal-left`
- **Local helpers inside `\where`**: `h-idemp`, `ipow_-`, `contains-x^-1*x*y`

### 1.3 Mixed camelCase with Separator Characters

The library uses a rich vocabulary of separator characters inside camelCase names to encode algebraic structure:

- **Underscore `_`** separates a function from its argument type or the law it encodes:
  - `pow_+`, `pow_*`, `BigProd_++`, `BigProd_ide`, `length_++`, `map_id`, `+-assoc`, `zro_*-left`
- **Hyphen `-`** separates components of compound names or algebraic roles:
  - `ide-left`, `ide-right`, `inverse-left`, `inverse-right`, `meet-left`, `meet-right`, `meet-comm`, `cancel-left`, `zro-left`, `zro-right`
- The underscore and hyphen are **not interchangeable**: underscores denote "applied to" relationships (`pow_+` = "pow respects +"), hyphens denote positional or directional roles (`ide-left` = "identity law on the left").

### 1.4 Single-letter Identifiers

Single lowercase letters are used universally for term variables. There is no fixed convention for letters, but common patterns include:

- `x, y, z` for elements of a type/set
- `n, m, k` for natural numbers
- `a, b, c` for generic algebraic elements
- `p, q, r` for proofs/equalities
- `f, g, h` for functions
- `i, j` for indices (typically `Fin n`)
- `e` for equivalences or neutral elements in context

### 1.5 Operator / Symbolic Names

Operators are defined with `\infixl`, `\infixr`, or `\infix` fixity declarations and often given both an ASCII name and a Unicode alias via `\alias`:

- `\infixl 7 *` — multiplication
- `\infixr 5 ::` — cons
- `\infixr 5 ++` — concatenation
- `\infix 4 <=` — partial order
- `\infixl 7 ∧` (alias for `meet`)
- `\infixl 8 ∘` (alias for `compose` or `o`)
- `\infix 4 ⊆` (alias for `Subset`)
- `\infixr 9 <=∘` (alias for `<=-transitive`)

**Pattern**: Every operator that could be ambiguous in composition gets a fixity number. Looser binding has smaller numbers (4 for order, 5 for cons/append, 6 for additive, 7 for multiplicative, 8 for composition).

### 1.6 Instances

`\instance` declarations use a descriptive PascalCase name combining the type with the structure being instantiated:

- `NatSemiring`, `IntRing`, `RatField`, `BoolLattice`, `ListMonoid`, `SetCat`, `SetLattice`

**Pattern**: The instance name is `<Type><Structure>`, where both parts are PascalCase.

---

## 2. Structural Conventions

### 2.1 `\where` Clauses

`\where` clauses are used extensively for three distinct purposes:

**a) Scoped helper definitions** — helpers used only in the proof above are placed in a `\where` block immediately following the enclosing definition:

```arend
\lemma ipow_+ ... \where {
  \open Arith.Int.IntRing(+,+-comm)
  \lemma ipow_- {a : E} ... => ...
}
```

**b) Namespace groupings** — when a group of closely related definitions is logically associated with a type, they are placed in the type's `\where` block even if they are standalone:

```arend
\record MonoidHom ... \where {
  \func equals ...
  \func id ...
  \func presInv ...
}
```

**c) `\module` groupings** — standalone `\module Name \where { ... }` blocks are used to group topically related utilities that do not belong to any specific `\class` or `\record`:

```arend
\module NatOrder \where { ... }
\module Sort \where { ... }
```

### 2.2 File-to-Module Naming

Each `.ard` file typically contains one primary `\class`, `\record`, `\instance`, or `\data` whose name matches or closely corresponds to the file name:

- `Monoid.ard` → `\class Monoid`
- `Ring.ard` → `\class Ring`
- `PartialOrder.ard` → `\class Preorder`, `\class Poset`
- `MonoidHom.ard` → `\record MonoidHom`

Auxiliary definitions closely related to the primary definition are co-located in the same file rather than split into separate files, unless the auxiliary material is large enough to warrant its own file (e.g., `Monoid/GCD.ard`, `Ring/Ideal.ard`).

### 2.3 Directory Structure

Directories correspond to mathematical domains:

- `Algebra/` — algebraic structures (further subdivided by structure type)
- `Order/` — ordered structures
- `Arith/` — concrete arithmetic types (Nat, Int, Rat, Real)
- `Data/` — data structures (List, Array, Maybe, etc.)
- `Equiv/` — equivalences and homotopy theory
- `Set/` — set-theoretic utilities
- `Logic/` — logic and formal reasoning
- `Category/`, `Topology/`, `Homotopy/`, `AG/` — more advanced mathematical areas

Sub-domain specializations add another layer: `Algebra/Ring/`, `Algebra/Group/`, `Algebra/Monoid/`, `Algebra/Domain/`, etc.

### 2.4 Ordering of Declarations Within Files

The typical order within a file is:

1. `\import` statements (one per line, alphabetically within groups)
2. `\open` statements for frequently used names
3. The primary `\class`/`\record`/`\data` definition
4. Derived classes that extend the primary one
5. `\instance` declarations
6. Top-level lemmas / functions that use the above
7. Longer helpers in `\where` blocks or separate `\module` blocks

---

## 3. Mathematical Notation Style

### 3.1 `\lemma` vs `\func`

- **`\lemma`** is used for propositions (proofs of properties, equalities, inequalities). It lives in `\Prop` and benefits from proof irrelevance.
- **`\func`** is used for computational content (constructions, data transformations, type-valued operations).
- **`\instance`** is used for typeclass instances.
- **`\class`/`\record`** is used for mathematical structures.

The distinction is respected strictly: a proof of `x = y` is always a `\lemma`, while a function producing an element is always a `\func`.

### 3.2 `AddX` vs Multiplicative Naming

The library systematically duplicates algebraic structures into additive (`Add`) versions:

- `Monoid` / `AddMonoid`
- `Group` / `AddGroup`
- `Semigroup` / `AddSemigroup`
- `MonoidHom` / `AddMonoidHom`
- `ide` / `zro` (identity elements)
- `*` / `+` (binary operations)
- `inverse` / `negative`

The `Add` prefix is always prepended to the class name, and additive-specific names use `+`, `zro`, `negative` instead of `*`, `ide`, `inverse`.

### 3.3 Abbreviations

Common abbreviations used pervasively:

| Abbreviation | Meaning |
|---|---|
| `ide` | identity element |
| `zro` | zero element |
| `inv` | inverse (in proofs) or path inverse |
| `distr` | distributivity |
| `assoc` | associativity |
| `comm` | commutativity |
| `func` | a field/method of a homomorphism record |
| `pmap` | path map (apply function to path) |
| `idp` | identity path |
| `inP` | constructor of `TruncP` (truncated proposition) |
| `in~` | constructor of `Quotient` |
| `LDiv` | left divisibility |
| `Inv` | invertibility |
| `Mon` / `CMonoid` | (commutative) monoid |
| `CRing` | commutative ring |

### 3.4 Unicode vs ASCII

The library uses Unicode freely for mathematical notation but always provides an ASCII alias via `\alias` for operator names that might be composed programmatically. Unicode appears in:

- Order: `<=`, `<`, `∧`, `∨`, `⊆`, `<=∘`
- Algebra: `∘` (composition), `⨯` (product), `⨿` (coproduct)
- Logic: `∃`, `∀`, `⊥` (in propositions)

Pure ASCII names (`meet`, `join`, `compose`, `ldistr`) are always available as alternatives.

---

## 4. Definitions and Proof Patterns

### 4.1 Standard Algebraic Law Suffixes

The library follows consistent naming for algebraic laws:

| Suffix | Law |
|---|---|
| `-assoc` | associativity: `(x * y) * z = x * (y * z)` |
| `-comm` | commutativity: `x * y = y * x` |
| `-left` | left identity/annihilation/inverse |
| `-right` | right identity/annihilation/inverse |
| `-idemp` | idempotency |
| `-monotone` | monotonicity |
| `_<= ` | implies the ordering relation |
| `-unique` | uniqueness |
| `-univ` | universal property |
| `_+` / `_*` | interaction with addition/multiplication |

Examples: `ide-left`, `ide-right`, `inverse-left`, `inverse-right`, `meet-left`, `meet-right`, `meet-assoc`, `meet-comm`, `meet-idemp`, `pow_+`, `pow_*`.

### 4.2 `func-` Prefix in Homomorphisms

Every field in a homomorphism record that witnesses preservation of structure is prefixed with `func-`:

- `func-ide` — preserves identity
- `func-*` — preserves multiplication
- `func-+` — preserves addition
- `func-BigProd`, `func-BigSum` — preserves big products/sums
- `func-pow` — preserves powers
- `func-LDiv` — preserves left divisibility

### 4.3 `contains_` Prefix in Sub-structures

Fields and lemmas in sub-structure records (`SubMonoid`, `SubGroup`, `SubSemigroup`, etc.) use `contains_` to name closure conditions:

- `contains_*` — closed under multiplication
- `contains_ide` — contains the identity
- `contains_inverse` — closed under inverses
- `contains_pow` — closed under powers
- `contains_zro`, `contains_negative` — for additive variants

### 4.4 Equational Proof Style

Equational chain proofs use the `==<` and `>==` notation (Arend's built-in calculation block):

```arend
y   ==< inv ide-left >==
ide * y   ==< pmap (`* y) (inv inverse-left) >==
(inverse x * x) * y   `qed
```

Short proofs compose lemmas inline with `*>` (forward path composition) and `inv` (path reversal):

```arend
pmap (`* a) pow_+ *> *-assoc
```

### 4.5 `op` for Opposite Structures

Every algebraic class that has a natural opposite/dual construction provides a `\protected \func op` that builds the opposite structure by swapping operations. This is consistent across `Preorder`, `Poset`, `Monoid`, `Group`, `Semiring`, `PseudoRing`, `Precat`, etc.:

```arend
\protected \func op : Monoid E \cowith
  | ide => ide
  | * x y => y * x
  | *-assoc => inv *-assoc
```

The `\protected` modifier prevents accidental name clashes when the `op` is opened.

### 4.6 `from`/`to` Coercions

`\use \coerce` declarations follow a `fromX`/`toX` naming convention for canonical conversions between related types:

- `fromPointed`, `toPointed`
- `fromGroup`, `fromMonoid`
- `fromRat`, `fromInt`
- `fromQEquiv`, `fromEquiv`
- `toMonoidHom`

The direction `fromX` means "construct this type from X", `toX` means "convert to X".

---

## 5. Argument and Type Conventions

### 5.1 Implicit vs Explicit Arguments

- **Implicit `{}`** arguments are used for:
  - Universe-polymorphic type parameters that are inferrable: `{A : \Type}`, `{n : Nat}`
  - Arguments that are uniquely determined by later arguments (e.g., length of an array, element type)
  - Proof arguments when the proof is to be inferred: `{x y z : E}` in `*-assoc`
- **Explicit `()`** arguments are used for:
  - Arguments the caller must supply: function inputs, indices, explicit structures
  - Arguments that are not inferrable or where inference would be ambiguous

**Pattern**: Field declarations in classes use implicit `{}` for the typed variables in the law statement but explicit `()` for the class type parameter itself.

### 5.2 `\override` in Substructure Records

`\override` is used in record extensions to refine the type of an inherited field to a more specific class:

```arend
\record MonoidHom \extends PointedHom {
  \override Dom : Monoid
  \override Cod : Monoid
  ...
}
```

This is the standard way to specialize homomorphism records without re-declaring the carrier.

### 5.3 Argument Ordering in Class Fields

In class declarations, the convention is:

1. The carrier type or set (often implicit, inherited from `BaseSet` via `E`)
2. Operations (infix declarations)
3. Laws (as `\Prop`-valued fields, nearly always implicit arguments)

### 5.4 Universe Levels

Universe polymorphism is expressed with `\plevels` declarations at the top of files when needed:

```arend
\plevels obj >= hom
```

Level parameters appear explicitly in class declarations (`Precat (\lp,\lp)`) when the class is level-polymorphic.

### 5.5 `\coerce` Conversions

`\use \coerce` (within a `\where` block of the target type) provides implicit coercions. Naming follows the `fromX` pattern. This is used to make the type hierarchy transparent: for example, `AddMonoid` and `Monoid` can be used interchangeably in appropriate contexts.

---

## 6. Documentation and Comment Style

### 6.1 Inline Block Comments `{- ... -}`

Block comments `{- ... -}` are used as inline documentation comments for individual definitions. They appear most commonly as the first line of a definition or immediately before it:

```arend
{- | Associative ring -}
\class PseudoRing ...

{- | Left ideal -}
\record LIdeal ...
```

The `{- | ... -}` form (with a leading pipe character) is used for Haddock-style documentation that is rendered by tooling.

### 6.2 Line Comments `-- |`

Line comments `-- |` are used as documentation comments before definitions, especially for `\func` and `\lemma` declarations:

```arend
-- | If ``f : A -> B`` is an equivalence, then ``pmap f`` is also an equivalence.
\func pmapEquiv ...

-- | The intermediate value theorem for strictly monotone functions.
\lemma ivt ...
```

Double-backtick `` ``name`` `` syntax is used within `-- |` doc comments to reference identifiers.

### 6.3 Placement

Documentation comments are placed immediately before the definition they document with no blank line between comment and definition. Comments appear before both top-level and `\where`-local definitions.

### 6.4 Section Comments

Larger thematic groupings within a file are sometimes marked with a section comment using `-- # Section Name`:

```arend
-- # Various operations
\func ...

-- # The order relations
\module NatOrder \where { ... }
```

### 6.5 Inline Remarks

Short informal remarks explaining non-obvious steps are placed as `-- comment` on the same line or just before a clause.

---

## 7. Formatting and Layout Conventions

### 7.1 Indentation

- 2-space indentation is standard for the body of `\class`, `\record`, `\func`, and `\where` blocks.
- Nested `\where` blocks add 2 more spaces per level.

### 7.2 `\import` Ordering

`\import` declarations appear at the top of the file, one per line, typically in roughly alphabetical order within logical groups (core modules first, then more specialized ones).

### 7.3 Pattern Matching Layout

`\elim` and `\with` pattern matching uses vertical alignment of cases:

```arend
| 0, _ => 0
| suc n, 0 => suc n
| suc n, suc m => n -' m
```

### 7.4 Equational Proof Layout

Long equational proofs use the `==< ... >==` chained-equality notation with each step on its own line:

```arend
y          ==< inv ide-left >==
ide * y    ==< ... >==
...        `qed
```

Short one-step proofs use inline `*>` composition.

### 7.5 `\cowith` vs `\new`

- `\cowith` is used when providing a record implementation at the top level of a `\func`, `\instance`, or `\lemma` result.
- `\new` is used inline when constructing a record value as an expression.

### 7.6 Operator Section Syntax

Lambda-section syntax is used frequently:

- `` `* a `` for "right-multiply by a"
- `` x * __ `` for "left-multiply by x"
- `` `+ b `` for "right-add b"

---

## 8. Consistency Rules

### 8.1 Capitalization Encodes Kind

| What | Convention | Example |
|---|---|---|
| Types/classes | PascalCase | `Monoid`, `Ring`, `Preorder` |
| Constructors | PascalCase | `LIdeal`, `RIdeal`, `GCD` |
| Functions/lemmas | camelCase | `inverse-left`, `func-ide`, `pow_+` |
| Instances | PascalCase suffix | `NatSemiring`, `IntRing`, `ListMonoid` |
| Module blocks | PascalCase | `NatOrder`, `Sort`, `TwoOutOfThree` |
| Variables | lowercase single letter | `x`, `n`, `f`, `p` |

### 8.2 `Add` Prefix for Additive Counterparts

Every multiplicative structure has an additive counterpart obtained by prepending `Add`. Operations rename as: `*` → `+`, `ide` → `zro`, `inverse` → `negative`. This pattern is unbroken across the entire library.

### 8.3 `Sub` Prefix for Sub-structures

Sub-structure records always use the `Sub` prefix: `SubMonoid`, `SubGroup`, `SubSemigroup`, `SubRing`, `SubAddGroup`. They extend both the `SubSet`/`SubPointed` hierarchy and the parent algebraic structure.

### 8.4 `Hom` Suffix for Homomorphisms

Homomorphism records consistently use the `Hom` suffix: `MonoidHom`, `AddMonoidHom`, `GroupHom`, `RingHom`, `SemiringHom`, `LinearMap`, `PointedHom`.

### 8.5 `-left` / `-right` Directionality

For any binary operation, laws involving only one side are always paired:
- `ide-left` and `ide-right`
- `inverse-left` and `inverse-right`
- `cancel_*-left` and `cancel_*-right`
- `zro_*-left` and `zro_*-right`
- `meet-left` and `meet-right`

The `-left` variant always refers to the left argument of the operation.

### 8.6 `\protected` on `op` and Internal Helpers

The `\protected` modifier is used on `op` (opposite structure) and on internal helper lemmas that should not be opened globally but are accessible via qualified names:

```arend
\protected \func op : Monoid E \cowith ...
\protected \lemma isDefined ...
\protected \lemma value ...
```

### 8.7 `\open` Usage

`\open StructureName` at the top of a file or inside a `\where` block selectively imports names from another definition. When only specific names are needed, the selective import `\open Module(name1, name2)` is preferred:

```arend
\open Monoid(LDiv,Inv)
\open AddMonoid
\open Group \hiding (Dec)
```

### 8.8 Canonical Algebraic Law Names

The following names are fixed across all algebraic structures:

| Name | Law |
|---|---|
| `*-assoc` / `+-assoc` | associativity |
| `*-comm` / `+-comm` | commutativity |
| `ide-left` / `zro-left` | left identity |
| `ide-right` / `zro-right` | right identity |
| `inverse-left` / `negative-left` | left inverse |
| `inverse-right` / `negative-right` | right inverse |
| `ldistr` | left distributivity: `x * (y + z) = x*y + x*z` |
| `rdistr` | right distributivity: `(x + y) * z = x*z + y*z` |
| `meet-assoc` / `join-assoc` | lattice associativity |
| `meet-comm` / `join-comm` | lattice commutativity |
| `meet-idemp` / `join-idemp` | idempotency |

---

## 9. Observed Style Guide (Inferred)

The following is a condensed, actionable guide for contributors writing new code consistent with arend-lib.

### Naming

1. **Use PascalCase** for all type-level definitions: classes, records, data types, instances, module blocks.
2. **Use camelCase with hyphens or underscores** for all term-level definitions: functions, lemmas, fields.
3. **Use hyphen `-`** to separate positional/directional qualifiers: `-left`, `-right`, `-assoc`, `-comm`.
4. **Use underscore `_`** to denote an interaction or relationship: `pow_+` means "pow distributes over +", `length_++` means "length of concatenation".
5. **Prefix additive variants with `Add`**: `AddMonoid`, `AddGroupHom`, `func-+`, `zro-left`.
6. **Prefix sub-structures with `Sub`**: `SubMonoid`, `SubGroup`.
7. **Suffix homomorphisms with `Hom`**: `MonoidHom`, `RingHom`.
8. **Name instances as `<Type><Structure>`**: `NatSemiring`, `ListMonoid`.
9. **Use `fromX`/`toX` for coercions**: `fromRat`, `toMonoidHom`.

### Structure

10. **Each file contains one primary definition** whose name matches the filename.
11. **Use `\where` blocks** for helpers tightly coupled to one definition; use top-level `\module` blocks for standalone groupings.
12. **Place `\protected` on `op`** (opposite structure) and on implementation-internal helpers to prevent accidental opening.
13. **Use `\override`** in record extensions to refine inherited field types.
14. **Provide both ASCII and Unicode names** via `\alias` for operators used in fixity position.

### Proofs

15. **Use `\lemma`** for all propositional content (proofs), **use `\func`** for computations.
16. **Use `==< ... >==` chains** for multi-step equational reasoning; use `*>` and `inv` for short inline chains.
17. **Follow the canonical law-name vocabulary** (`*-assoc`, `ide-left`, `ldistr`, etc.) even for new structures that extend existing ones.
18. **Prefix homomorphism-preservation fields with `func-`**: `func-ide`, `func-*`, `func-BigSum`.
19. **Prefix containment lemmas with `contains_`** in sub-structure records.

### Documentation

20. **Use `{- | ... -}`** for block-level documentation on classes, records, and data types.
21. **Use `-- |`** for line-level documentation on functions and lemmas.
22. **Use ` ``name`` `** inside doc comments to reference code identifiers.
23. **Use `-- # Section`** comments to delineate major thematic groupings within large files.
