# Notation and Style Conventions in arend-lib

This document describes the notational and stylistic conventions observed throughout the Arend standard library (`arend-lib`), based on analysis of 333 `.ard` source files under `src/`.

---

## 1. Naming Conventions

### 1.1 Case Styles by Declaration Type

#### PascalCase
Used for:
- **Classes and records**: `Semigroup`, `Monoid`, `Group`, `Preorder`, `Poset`, `DecSet`, `BaseSet`
- **Data types**: `TruncP`, `ToProp`, `Trunc0`, `Empty`
- **Type predicates and properties**: `IsInj`, `IsSurj`, `IsJoin`, `IsMeet`, `IsNilpotent`, `IsBezout`, `IsVonNeumannRegular`, `IsZeroDimensional`
- **Instances**: `ListMonoid`, `DecBool`, `ProductDecSet`, `ArrayDec`, `EmptyNegated`
- **Constructors (data)**: Often PascalCase or descriptive names like `SplitMono`, `Retraction`, `Section`

**Examples:**
```arend
\class Monoid \extends Pointed, Semigroup
\data TruncP (A : \Type)
\func IsInj {A B : \Set} (f : A -> B)
\instance ListMonoid {A : \Set} : Monoid (List A)
```

#### camelCase
Used for:
- **Functions**: `pmap`, `transport`, `idEquiv`, `mkArray`, `arrayExt`, `headDef`, `splitAt`
- **Lemmas and proofs** (when not using kebab-case): `makeInv`, `fromEquiv`, `toFin`, `decToBool`
- **Meta functions**: `assuming`, `flip`

**Examples:**
```arend
\func pmap {A B : \Type} (f : A -> B) {a a' : A} (p : a = a')
\func mkArray {A : \Type} {n : Nat} (f : Fin n -> A)
\func headDef {A : \Type} (x : A) (xs : List A) : A
```

#### kebab-case (hyphenated)
Used extensively for:
- **Class/record fields**: `*-assoc`, `ide-left`, `ide-right`, `inverse-left`, `inverse-right`, `<=-refl`, `<=-transitive`, `<=-antisymmetric`
- **Lemmas**: `prop-pi`, `prop-isProp`, `set-pi`, `meet-comm`, `meet-assoc`, `join-comm`, `join-assoc`, `top-left`, `bottom-right`, `compl-inv`
- **Properties with operators**: `#-irreflexive`, `#-symmetric`, `#-comparison`

**Examples:**
```arend
| *-assoc {x y z : E} : (x * y) * z = x * (y * z)
| ide-left {x : E} : ide * x = x
\lemma prop-pi {A : \Prop} {a a' : A} : a = a'
\lemma meet-comm {x y : E} : x ∧ y = y ∧ x
```

#### underscore_separated
Used for:
- **Lemmas involving operators or specific operations**: `pow_+`, `pow_*`, `pow_ide`, `length_++`, `length_map`, `map_id`, `map_comp`, `BigProd_++`, `BigProd_suc`
- **Lemmas with negation or inverse**: `inverse_*`, `inverse_ide`, `inverse_pow`
- **Reduction lemmas**: `ret_f`, `f_sec`, `f_ret`

**Examples:**
```arend
\lemma pow_+ {a : E} {n m : Nat} : pow a (n + m) = pow a n * pow a m
\lemma length_++ {A : \Type} {l l' : List A} : length (l ++ l') = length l Nat.+ length l'
\lemma map_id {A : \Type} {l : List A} : map (\lam x => x) l = l
```

#### lowercase
Used for:
- **Data constructors**: `nil`, `idp`, `inP`, `yes`, `no`, `byLeft`, `byRight`, `inl`, `inr`, `true`, `false`
- **Module-level functions**: `absurd`, `id`
- **Derived structures**: `subPoset`

**Examples:**
```arend
\data List (A : \Type)
  | nil
  | \infixr 5 :: A (List A)

\data Dec (E : \Prop)
  | yes E
  | no (Not E)
```

#### Symbolic/Operator Names
Used for:
- **Infix operators**: `*`, `+`, `-`, `<=`, `>=`, `<`, `>`, `∧`, `∨`, `*>`, `<*`, `==`, `/=`, `#`, `||`, `<->`
- **Composition operators**: `o`, `∘`, `-o`, `o-`, `>>`
- **Special operators**: `!!` (indexing), `++` (concatenation)

**Examples:**
```arend
\func \infixr 9 *> {A : \Type} {a a' a'' : A} (p : a = a') (q : a' = a'')
\func \infixr 8 o {A B C : \Type} (g : B -> C) (f : A -> B)
\func \infixl 9 !! {A : \Type} (l : List A) (i : Fin (length l)) : A
```

### 1.2 Single-Letter Identifiers

Common in:
- **Type parameters**: `A`, `B`, `C`, `E`, `J`, `P`, `Q`, `S`
- **Element variables**: `x`, `y`, `z`, `a`, `b`, `c`, `n`, `m`, `i`, `j`, `k`
- **Function parameters**: `f`, `g`, `h`, `p`, `q`, `r`, `s`, `t`

**Pattern**: Type parameters typically use uppercase; value parameters use lowercase.

### 1.3 Naming Patterns and Suffixes

#### Common Suffixes
- **`-left` / `-right`**: Sidedness properties
  - `ide-left`, `ide-right`, `inverse-left`, `inverse-right`
  - `top-left`, `top-right`, `bottom-left`, `bottom-right`
  - `negative_*-left`, `negative_*-right`

- **`-comm`**: Commutativity
  - `meet-comm`, `join-comm`, `+-comm`

- **`-assoc`**: Associativity
  - `*-assoc`, `meet-assoc`, `join-assoc`, `++-assoc`, `*>-assoc`

- **`-inv`**: Inverse properties
  - `inv_inv`, `inv_*>`, `*>_inv`, `compl-inv`

- **`-refl`**: Reflexivity
  - `<=-refl`

- **`-transitive`**: Transitivity
  - `<=-transitive`

- **`-antisymmetric`**: Antisymmetry
  - `<=-antisymmetric`

- **`-symmetric`**: Symmetry
  - `#-symmetric`

- **`-irreflexive`**: Irreflexivity
  - `#-irreflexive`

#### Common Prefixes
- **`Big`**: Aggregation operations
  - `BigProd`, `BigSum`, `Big_meet`, `Big_join`, `Big_∧`, `Big_∨`

- **`is`**: Boolean predicates
  - `isMono`, `isEpi`, `isInj`, `isSurj`, `isNegated`

- **`Is`**: Type-level predicates (PascalCase)
  - `IsInj`, `IsSurj`, `IsJoin`, `IsMeet`, `IsSquare`, `IsNilpotent`

- **`make`**: Constructor functions
  - `makeInv`, `makeUniform`

- **`from`**: Conversion functions
  - `fromEquiv`, `fromInjSurj`, `fromProp`

- **`to`**: Conversion functions
  - `toFin`, `toOr`, `toProp`

#### Variants with Apostrophe
Apostrophe (`'`) suffix indicates a variant or alternative implementation:
- `++` vs `++'` (different type signatures for concatenation)
- `toFin` vs `toFin'`
- `fromEquiv` vs `fromEquiv'`

**Examples:**
```arend
\func \infixr 5 ++ {A : \Type} (xs ys : Array A) : Array A
\func \infixr 5 ++' {A : \Type} (xs : Array A) {n : Nat} (ys : Array A n) : Array A (xs.len Nat.+ n)
```

---

## 2. Structural Conventions

### 2.1 The `\where` Clause

The `\where` clause is used extensively to group related definitions, helper functions, and lemmas with their parent definition.

#### Usage Patterns

**Helper lemmas and functions:**
```arend
\func splitAt {A : \Type} (n : Nat) (l : List A) : \Sigma (List A) (List A)
  \where
    \func appendLem {A : \Type} (n : Nat) (l : List A) : take n l ++ drop n l = l
```

**Alternative implementations:**
```arend
\func Jl {A : \Type} {a : A} (B : \Pi (a' : A) -> a = a' -> \Type) (b : B a idp) {a' : A} (p : a = a') : B a' p
  \where {
    \func Jr {A : \Type} {a' : A} (B : \Pi (a : A) -> a = a' -> \Type) (b : B a' idp) {a : A} (p : a = a') : B a p
    
    \func def {A : \Type} {a : A} (B : \Pi (a' : A) -> a = a' -> \Type) (b : B a idp) {a' : A} (p : a = a') : B a' p
  }
```

**Nested structures and instances:**
```arend
\class Monoid \extends Pointed, Semigroup
  \where {
    \protected \func equals {M N : Monoid} (p : M = {\Set} N) ...
      \where {
        \lemma ide-equality : coe (p @) ide right = ide
      }
  }
```

**Proof helpers:**
```arend
\lemma ipow_+ {a : E} {x y : Int} : ipow a (x + y) = ipow a x * ipow a y
  \where {
    \open Arith.Int.IntRing(+,+-comm)
    
    \lemma ipow_- {a : E} {n m : Nat} : ipow a (n Nat.- m) = pow a n * pow (inverse a) m
  }
```

#### Naming Inside `\where`
- Helper lemmas often have descriptive names related to their parent
- Common pattern: `parentName_property` or standalone descriptive names
- `\private` modifier used for internal helpers not meant for export

### 2.2 Module Organization

#### `\module` for Grouping
Used to create namespaces for related definitions:

```arend
\module NatOrder \where {
  \data \infix 4 < (n m : Nat) \with
    | 0, suc _ => zero<suc
    | suc n, suc m => suc<suc (n < m)
  
  \lemma unsuc< {n m : Nat} (p : suc n < suc m) : n < m
}
```

#### `\open` for Importing
Selective import of names from modules:

```arend
\open Nat
\open LinearlyOrderedAbMonoid
\open NatOrder
```

With selective import:
```arend
\import Order.PartialOrder \hiding (<=)
\import Function.Meta ($)
```

### 2.3 File and Module Naming

**Consistent pattern**: File name matches the primary definition or module name.

Examples:
- `src/Paths.ard` — path equality operations
- `src/Algebra/Monoid.ard` — `Monoid` class
- `src/Algebra/Group.ard` — `Group` class
- `src/Data/List.ard` — `List` data type
- `src/Set.ard` — set-related classes (`DecSet`, `BaseSet`, etc.)
- `src/Order/PartialOrder.ard` — `Preorder` and `Poset` classes

**Directory structure** reflects mathematical hierarchy:
- `Algebra/` — algebraic structures
- `Order/` — ordered structures
- `Topology/` — topological structures
- `Data/` — data structures
- `Logic/` — logical foundations

### 2.4 Declaration Ordering

Typical ordering within files:
1. Imports
2. Core definitions (data types, classes, records)
3. Basic operations and constructors
4. Properties and lemmas
5. Instances
6. Derived structures
7. `\where` clauses with helpers

---

## 3. Mathematical Notation Style

### 3.1 Lemmas vs Theorems

**Observation**: The library uses `\lemma` extensively; `\theorem` is rarely or never used.

**Convention**: All proved statements use `\lemma`, regardless of importance.

### 3.2 Proof Helper Naming

Proof helpers follow these patterns:
- Descriptive names based on what they prove
- Often placed in `\where` clauses
- Use kebab-case or underscore notation
- May include property suffixes (`-left`, `-right`, `-comm`, etc.)

### 3.3 Operator and Infix Notation

#### Precedence Levels
Operators are defined with explicit precedence:

```arend
\func \infixl 7 * : E -> E -> E
\func \infixr 9 *> {A : \Type} {a a' a'' : A} (p : a = a') (q : a' = a'')
\func \infixr 8 o {A B C : \Type} (g : B -> C) (f : A -> B)
\func \infix 4 <= : E -> E -> \Prop
\func \infix 1 /= {A : \Type} (a a' : A)
\func \infix 0 <-> (P Q : \Prop)
```

**Common precedence levels:**
- `0-1`: Logical connectives (`<->`, `/=`)
- `2`: Equality reasoning (`qed`, `==<`)
- `4`: Comparisons (`<`, `<=`, `>=`, `>`, `#`)
- `5`: Concatenation (`::`, `++`)
- `6-7`: Additive/multiplicative (`+`, `-`, `*`)
- `8`: Composition (`o`, `∘`)
- `9`: Path composition (`*>`, `<*`, `<=∘`)

#### Fixity
- `\infixl`: Left-associative (e.g., `*`, `!!`)
- `\infixr`: Right-associative (e.g., `*>`, `::`, `++`)
- `\infix`: Non-associative (e.g., `<=`, `==`)
- `\fixl`, `\fixr`: Alternative syntax

### 3.4 Unicode vs ASCII

**Heavy Unicode usage** for mathematical symbols:

**Logical operators:**
- `∃` (exists), `∀` (forall)
- `∧` (and), `∨` (or)
- `||` (propositional or)

**Order relations:**
- `≤`, `≥` (alongside ASCII `<=`, `>=`)

**Composition:**
- `∘` (alongside ASCII `o`)

**Special symbols:**
- `-->` (implication in Heyting algebras)
- `<=∘` (transitive composition)

**Convention**: Unicode is preferred for standard mathematical notation, but ASCII alternatives often coexist.

### 3.5 Aliases

Multiple names for the same definition using `\alias`:

```arend
\func <=-transitive \alias \infixr 9 <=∘ {x y z : E} : x <= y -> y <= z -> x <= z

\func Big_meet \alias Big_∧ {n : Nat} (l : Array E (suc n)) : E

\func \fixl 8 o \alias \infixl 8 ∘ {X Y Z : Ob} : Hom Y Z -> Hom X Y -> Hom X Z
```

**Pattern**: Provide both descriptive name and symbolic operator.

---

## 4. Definition and Proof Patterns

### 4.1 Helper Lemmas

Helper lemmas are commonly defined:
- In `\where` clauses
- With descriptive names
- Often marked `\private` if internal

**Example:**
```arend
\func splitAt {A : \Type} (n : Nat) (l : List A) : \Sigma (List A) (List A)
  \where
    \func appendLem {A : \Type} (n : Nat) (l : List A) : take n l ++ drop n l = l
```

### 4.2 Equational Reasoning

Proofs use equational reasoning chains with special operators:

```arend
\func cancel_*-left x {y} {z} p =>
  y                   ==< inv ide-left >==
  ide * y             ==< pmap (`* y) (inv inverse-left) >==
  (inverse x * x) * y ==< *-assoc >==
  inverse x * (x * y) ==< pmap (inverse x *) p >==
  inverse x * (x * z) ==< inv *-assoc >==
  (inverse x * x) * z ==< pmap (`* z) inverse-left >==
  ide * z             ==< ide-left >==
  z                   `qed
```

**Operators:**
- `==<`: Step with justification
- `>==`: Step with justification (alternative direction)
- `` `qed ``: End of proof

**Pattern**: Each step shows the term, the transformation, and the justification.

### 4.3 Pattern Matching with `\elim`

Pattern matching uses `\elim` to specify which arguments are matched:

```arend
\func length {A : \Type} (l : List A) : Nat \elim l
  | nil => 0
  | :: a l => suc (length l)

\func transport2 {A B : \Type} (C : A -> B -> \Type) {a a' : A} {b b' : B} (p : a = a') (q : b = b') (c : C a b) : C a' b' \elim p, q
  | idp, idp => c
```

### 4.4 Standard Algebraic Law Names

Consistent naming for algebraic properties:
- **Associativity**: `-assoc` or `_assoc`
- **Commutativity**: `-comm` or `_comm`
- **Identity**: `ide-left`, `ide-right` or `_ide`
- **Inverse**: `inverse-left`, `inverse-right` or `_inv`
- **Distributivity**: `ldistr`, `rdistr`
- **Cancellation**: `cancel_*-left`, `cancel_*-right`

### 4.5 Symmetry Patterns

Functions often come in symmetric pairs:
- `map`, `map2`
- `pmap`, `pmap2`, `pmapd`
- `transport`, `transport2`, `transportInv`
- `index-left`, `index-right`
- `halving-left`, `halving-right`
- `negative_*-left`, `negative_*-right`

---

## 5. Argument and Type Conventions

### 5.1 Implicit vs Explicit Arguments

**Implicit arguments** (curly braces `{}`):
- Type parameters: `{A : \Type}`, `{B : \Type}`
- Inferred values: `{x y : E}`, `{n m : Nat}`
- Proofs and evidence: `{p : a = b}`

**Explicit arguments** (parentheses `()`):
- Primary data: `(l : List A)`, `(n : Nat)`
- Functions: `(f : A -> B)`
- Values that cannot be inferred

**Examples:**
```arend
\func pmap {A B : \Type} (f : A -> B) {a a' : A} (p : a = a') : f a = f a'

\func transport {A : \Type} (B : A -> \Type) {a a' : A} (p : a = a') (b : B a) : B a'
```

### 5.2 Argument Ordering

**Typical order:**
1. Type parameters (implicit)
2. Structure/class instances (implicit or explicit)
3. Functions or operations (explicit)
4. Primary data (explicit)
5. Proofs or properties (implicit or explicit)
6. Additional parameters (mixed)

**Example:**
```arend
\func transport {A : \Type} (B : A -> \Type) {a a' : A} (p : a = a') (b : B a) : B a'
              -- ^type      ^function        ^elements   ^proof      ^data
```

### 5.3 Universe Levels

Universe levels are specified using:
- `\Type` for general types
- `\Set` for sets (types with unique identity proofs)
- `\Prop` for propositions (types with at most one inhabitant)
- `\hType` for h-types with specified level
- `\plevels` for level constraints

**Examples:**
```arend
\plevels obj >= hom

\class Precat (Ob : \hType obj) {
  | Hom : Ob -> Ob -> \Set hom
}
```

### 5.4 Special Parameter Annotations

**`\property`**: Marks proof-relevant parameters
```arend
\func toFin (k : Nat) {n : Nat} (\property p : k < n) : Fin n
```

**`\classifying`**: Marks classifying fields in subsets
```arend
\class SubSet (S : BaseSet) (\classifying contains : S -> \Prop)
```

**`\coerce`**: Marks coercion functions
```arend
\protected \record Map {A B : \Type} (\coerce f : A -> B)
```

---

## 6. Documentation and Comment Style

### 6.1 Comment Syntax

**Single-line comments**: `-- `
```arend
-- # Definition of equivalences
```

**Section headers**: `-- # `
```arend
-- # Various operations
-- # The order relations
-- # Fin properties
-- # Examples of equivalences
-- # Embeddings and surjections
```

### 6.2 Documentation Patterns

**Minimal inline documentation**: Comments are sparse and used primarily for:
- Major section divisions
- Brief explanations of non-obvious constructs
- Grouping related definitions

**No docstrings**: Unlike many languages, Arend files in this library do not use extensive docstrings or documentation comments before definitions.

**Example:**
```arend
-- # Definition of equivalences

\protected \record Map {A B : \Type} (\coerce f : A -> B)

\record Section \extends Map
  | ret : B -> A
  | ret_f : \Pi (x : A) -> ret (f x) = x
```

### 6.3 Comment Placement

Comments typically appear:
- Before major sections
- Occasionally inline for clarification
- Rarely after definitions

---

## 7. Formatting and Layout Conventions

### 7.1 Indentation

**2-space indentation** is standard:

```arend
\func pow (a : E) (n : Nat) : E \elim n
  | 0 => ide
  | suc n => pow a n * a

\lemma pow_+ {a : E} {n m : Nat} : pow a (n + m) = pow a n * pow a m \elim m
  | 0 => inv ide-right
  | suc m => pmap (`* a) pow_+ *> *-assoc
```

### 7.2 Pattern Matching Layout

**Inline patterns** for simple cases:
```arend
\func pred (x : Nat) : Nat
  | zero => 0
  | suc x' => x'
```

**Multi-line patterns** for complex cases:
```arend
\func splitAt {A : \Type} (n : Nat) (l : List A) : \Sigma (List A) (List A) \elim n, l
  | 0, l => (nil, l)
  | suc _, nil => (nil, nil)
  | suc n, :: a l =>
      \let! (l1, l2) => splitAt n l
      \in (a :: l1, l2)
```

### 7.3 Proof Formatting

**Equational reasoning** uses aligned chains:
```arend
\func homotopy_app-comm {A : \Type} (f : A -> A) (h : \Pi (a : A) -> f a = a) (a : A) : h (f a) = pmap f (h a) =>
  h (f a)                             ==< pmap (h (f a) *>) (inv (*>_inv (h a))) >==
  h (f a) *> (h a *> inv (h a))       ==< inv (*>-assoc (h (f a)) (h a) (inv (h a))) >==
  (h (f a) *> h a) *> inv (h a)       ==< pmap (`*> inv (h a)) (inv (homotopy-isNatural f (\lam a => a) h (h a))) >==
  (pmap f (h a) *> h a) *> inv (h a)  ==< *>-assoc (pmap f (h a)) (h a) (inv (h a)) >==
  pmap f (h a) *> (h a *> inv (h a))  ==< pmap (pmap f (h a) *>) (*>_inv (h a)) >==
  pmap f (h a)                        `qed
```

### 7.4 Class and Record Layout

**Compact field definitions:**
```arend
\class Semigroup \extends BaseSet {
  | \infixl 7 * : E -> E -> E
  | *-assoc {x y z : E} : (x * y) * z = x * (y * z)
}
```

**With implementations:**
```arend
\instance ListMonoid {A : \Set} : Monoid (List A)
  | ide => nil
  | * => ++
  | ide-left => idp
  | ide-right => ++_nil
  | *-assoc => ++-assoc
```

### 7.5 Import Organization

Imports are listed at the top, typically:
- One import per line
- Grouped by category (implicit)
- Selective imports with `\hiding` or specific names

```arend
\import Algebra.Meta
\import Algebra.Monoid
\import Data.Array
\import Function.Meta ($)
\import Logic
\import Order.PartialOrder \hiding (<=)
\import Paths
\import Paths.Meta
```

---

## 8. Observed Style Guide (Inferred)

### 8.1 Naming Rules

1. **Classes, records, data types**: PascalCase
2. **Functions**: camelCase
3. **Lemmas**: kebab-case or underscore_case
4. **Class fields**: kebab-case (especially for operators and properties)
5. **Instances**: PascalCase
6. **Data constructors**: lowercase or PascalCase
7. **Type predicates**: PascalCase with `Is` prefix
8. **Boolean predicates**: camelCase with `is` prefix

### 8.2 Structural Rules

1. **Use `\where` clauses** for helper definitions, alternative implementations, and related lemmas
2. **Use `\module`** for grouping related definitions that form a coherent namespace
3. **File names match** primary definitions or module names
4. **Directory structure** reflects mathematical hierarchy
5. **Imports at top**, organized logically

### 8.3 Mathematical Conventions

1. **Use `\lemma`** for all proved statements (no `\theorem`)
2. **Algebraic laws** use standard suffixes: `-assoc`, `-comm`, `-left`, `-right`, `-inv`
3. **Operators** have explicit precedence and fixity
4. **Unicode symbols** preferred for standard mathematical notation
5. **Provide aliases** for both symbolic and descriptive names

### 8.4 Proof Conventions

1. **Equational reasoning** with `==<`, `>==`, and `` `qed ``
2. **Pattern matching** with explicit `\elim`
3. **Helper lemmas** in `\where` clauses
4. **Intermediate steps** with `\let` or `\have`

### 8.5 Type Conventions

1. **Type parameters** are implicit by default
2. **Proofs** are often implicit
3. **Primary data** is explicit
4. **Argument order**: types → structures → functions → data → proofs
5. **Universe levels** specified when needed (`\Type`, `\Set`, `\Prop`, `\hType`)

### 8.6 Documentation Conventions

1. **Minimal comments**: Use sparingly
2. **Section headers**: `-- # Description`
3. **No extensive docstrings**: Code is self-documenting through naming
4. **Comments for major sections** only

### 8.7 Formatting Conventions

1. **2-space indentation**
2. **Aligned equational reasoning**
3. **One import per line**
4. **Compact class/record definitions**
5. **Pattern matching**: inline for simple cases, multi-line for complex

### 8.8 Consistency Principles

1. **Capitalization matters**: `IsInj` (type predicate) vs `isInj` (boolean function)
2. **Naming distinguishes purpose**: data vs proofs vs functions
3. **Symmetry in naming**: `left`/`right`, `map`/`map2`, `transport`/`transportInv`
4. **Suffixes indicate properties**: `-comm`, `-assoc`, `-inv`, `-left`, `-right`
5. **Prefixes indicate categories**: `Big`, `Is`, `is`, `make`, `from`, `to`
6. **Apostrophe for variants**: `++` vs `++'`, `toFin` vs `toFin'`
7. **Underscore vs kebab**: underscores for operations (`pow_+`), kebab for properties (`ide-left`)

### 8.9 Special Keywords and Modifiers

- **`\protected`**: Limits visibility, used for opposite structures (`op`)
- **`\private`**: Internal helpers not for export
- **`\use`**: Special annotations (e.g., `\use \level`, `\use \coerce`)
- **`\default`**: Default implementations in classes
- **`\property`**: Proof-relevant parameters
- **`\classifying`**: Classifying fields in subsets
- **`\coerce`**: Implicit coercion functions
- **`\truncated`**: Truncated data types
- **`\level`**: Universe level specifications
- **`\meta`**: Meta-level functions and type abbreviations
- **`\type`**: Type aliases
- **`\alias`**: Alternative names for definitions
- **`\open`**: Import specific names
- **`\hiding`**: Exclude specific names from import

---

## Summary

The arend-lib codebase exhibits highly consistent conventions:

- **Naming** is systematic: PascalCase for types/classes, camelCase for functions, kebab-case for properties and lemmas
- **Structure** uses `\where` clauses extensively for organization
- **Mathematical notation** favors Unicode, explicit precedence, and standard algebraic naming
- **Proofs** use equational reasoning with clear step-by-step justification
- **Types** distinguish implicit/explicit carefully, with standard argument ordering
- **Documentation** is minimal, relying on clear naming and structure
- **Formatting** is consistent with 2-space indentation and aligned reasoning chains

These conventions create a coherent, readable, and maintainable mathematical library that balances formality with practical usability.
