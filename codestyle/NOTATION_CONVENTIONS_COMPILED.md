# arend-lib Notation and Style Conventions

*A unified, comprehensive style guide for contributors to the [JetBrains/arend-lib](https://github.com/JetBrains/arend-lib) codebase, synthesized from analysis of the full `src/` directory.*

---

## Table of Contents

1. [Naming Conventions](#1-naming-conventions)
2. [Structural Conventions](#2-structural-conventions)
3. [Mathematical Notation Style](#3-mathematical-notation-style)
4. [Definition and Proof Patterns](#4-definition-and-proof-patterns)
5. [Argument and Type Conventions](#5-argument-and-type-conventions)
6. [Documentation and Comment Style](#6-documentation-and-comment-style)
7. [Formatting and Layout Conventions](#7-formatting-and-layout-conventions)
8. [Quick Reference Summary](#8-quick-reference-summary)

---

## 1. Naming Conventions

### 1.1 PascalCase — Types, Classes, Records, Instances, Modules

PascalCase is reserved exclusively for **type-level entities**:

- **Class and record definitions**: `Monoid`, `Semigroup`, `Group`, `CancelMonoid`, `PseudoRing`, `MeetSemilattice`, `DecSet`, `BaseSet`
- **`\data` types**: `List`, `Poly`, `Preorder`, `Poset`, `TruncP`, `ToProp`, `Trunc0`, `Empty`
- **Type-level predicates** (prefixed with `Is`): `IsInj`, `IsSurj`, `IsJoin`, `IsMeet`, `IsNilpotent`, `IsBezout`, `IsSquare`, `IsZeroDimensional`
- **`\instance` declarations**: `NatSemiring`, `IntRing`, `RatField`, `BoolLattice`, `ListMonoid`, `SetCat`, `DecBool`, `ProductDecSet`
- **`\module` groupings**: `NatOrder`, `TwoOutOfThree`, `Transports`, `Sort`, `Insertion`, `RedBlack`
- **File names** mirror PascalCase: `Monoid.ard`, `Group.ard`, `Ring.ard`, `PartialOrder.ard`

**Instance naming pattern**: `<Type><Structure>` — both parts are PascalCase, e.g., `NatSemiring`, `ListMonoid`, `IntRing`.

```arend
\class Monoid \extends Pointed, Semigroup
\data TruncP (A : \Type)
\instance ListMonoid {A : \Set} : Monoid (List A)
```

### 1.2 camelCase — Functions and Computational Definitions

camelCase is used for **computational** (non-propositional) term-level definitions:

- **`\func` definitions**: `arrayExt`, `headDef`, `mkArray`, `ipow`, `pmap`, `transport`, `idEquiv`, `splitAt`, `decToBool`
- **Meta functions**: `assuming`, `flip`

```arend
\func pmap {A B : \Type} (f : A -> B) {a a' : A} (p : a = a')
\func mkArray {A : \Type} {n : Nat} (f : Fin n -> A)
\func headDef {A : \Type} (x : A) (xs : List A) : A
```

> **Note on lemmas**: When a `\lemma` encodes a computation-like relationship between operations (e.g., `pow_+`), it uses underscore notation (see §1.3). When it encodes a positional or structural property (e.g., `ide-left`), it uses kebab-case (see §1.3). Pure camelCase is reserved for `\func` definitions.

### 1.3 Separator Characters — Hyphens and Underscores

The two separator characters encode distinct semantic relationships and are **not interchangeable**:

#### Kebab-case (hyphen `-`)
Used in names of **class/record fields**, **structural properties**, and **lemmas naming laws** by their positional or relational role:

- `*-assoc`, `+-assoc`, `++-assoc` — associativity
- `ide-left`, `ide-right`, `zro-left`, `zro-right` — identity laws
- `inverse-left`, `inverse-right`, `negative-left`, `negative-right` — inverse laws
- `meet-comm`, `join-comm`, `meet-assoc` — lattice laws
- `<=-refl`, `<=-transitive`, `<=-antisymmetric` — order laws
- `#-irreflexive`, `#-symmetric`, `#-comparison` — apartness laws
- `cancel-left`, `cancel-right` — cancellation

```arend
| *-assoc {x y z : E} : (x * y) * z = x * (y * z)
| ide-left {x : E} : ide * x = x
\lemma meet-comm {x y : E} : x ∧ y = y ∧ x
```

#### Underscore `_`
Used in lemmas that state a **relationship between an operation and another operation or argument**, encoding "applied to" or "distributes over":

- `pow_+`, `pow_*`, `pow_ide` — pow interacts with +, *, ide
- `length_++`, `length_map` — length of concatenation/map
- `map_id`, `map_comp` — map applied to identity/composition
- `BigProd_++`, `BigProd_suc` — BigProd behavior
- `func-BigSum`, `func-BigProd` — homomorphism preserves BigSum/BigProd
- `contains_*`, `contains_ide`, `contains_inverse` — sub-structure closure

```arend
\lemma pow_+ {a : E} {n m : Nat} : pow a (n + m) = pow a n * pow a m
\lemma length_++ {A : \Type} {l l' : List A} : length (l ++ l') = length l Nat.+ length l'
```

> **Decision**: Both documents agree on the underscore/hyphen distinction. The rule is enforced here because it significantly aids readability: a reader can immediately tell from the separator whether a name is about a structural law (`ide-left`) or an operational interaction (`pow_+`). This distinction is especially important in a growing library where both categories multiply rapidly.

### 1.4 Canonical Algebraic Law Names

The following names are fixed across all algebraic structures and must not be deviated from:

| Name | Law |
|---|---|
| `*-assoc` / `+-assoc` | Associativity |
| `*-comm` / `+-comm` | Commutativity |
| `ide-left` / `zro-left` | Left identity |
| `ide-right` / `zro-right` | Right identity |
| `inverse-left` / `negative-left` | Left inverse |
| `inverse-right` / `negative-right` | Right inverse |
| `ldistr` | Left distributivity: `x * (y + z) = x*y + x*z` |
| `rdistr` | Right distributivity: `(x + y) * z = x*z + y*z` |
| `meet-assoc` / `join-assoc` | Lattice associativity |
| `meet-comm` / `join-comm` | Lattice commutativity |
| `meet-idemp` / `join-idemp` | Idempotency |
| `meet-left` / `meet-right` | Meet bounds |

### 1.5 Naming Prefixes and Suffixes

#### Structural Prefixes

| Prefix | Usage | Examples |
|---|---|---|
| `Add` | Additive counterpart of a multiplicative structure | `AddMonoid`, `AddGroup`, `AddGroupHom` |
| `Sub` | Sub-structure records | `SubMonoid`, `SubGroup`, `SubSemigroup`, `SubRing` |
| `Big` | Aggregation over a collection | `BigProd`, `BigSum`, `Big_meet`, `Big_join`, `Big_∧`, `Big_∨` |
| `Is` | Type-level predicates (PascalCase) | `IsInj`, `IsSurj`, `IsJoin`, `IsNilpotent` |
| `is` | Boolean/computable predicates (camelCase) | `isMono`, `isEpi`, `isInj`, `isNegated` |
| `make` | Constructor/builder functions | `makeInv`, `makeUniform` |
| `from` | Coercion into a type from another | `fromEquiv`, `fromInjSurj`, `fromRat`, `fromPointed` |
| `to` | Coercion out of a type to another | `toFin`, `toOr`, `toProp`, `toMonoidHom` |
| `func-` | Homomorphism preservation fields | `func-ide`, `func-*`, `func-+`, `func-BigSum` |
| `contains_` | Sub-structure closure fields/lemmas | `contains_*`, `contains_ide`, `contains_inverse` |

#### Structural Suffixes

| Suffix | Usage | Examples |
|---|---|---|
| `Hom` | Homomorphism records | `MonoidHom`, `AddMonoidHom`, `GroupHom`, `RingHom`, `SemiringHom` |
| `-left` / `-right` | Sidedness of a law | `ide-left`, `inverse-right`, `cancel-left` |
| `-assoc` | Associativity | `*-assoc`, `meet-assoc` |
| `-comm` | Commutativity | `+-comm`, `meet-comm` |
| `-inv` | Inverse property | `inv_inv`, `inv_*>`, `compl-inv` |
| `-refl` | Reflexivity | `<=-refl` |
| `-transitive` | Transitivity | `<=-transitive` |
| `-antisymmetric` | Antisymmetry | `<=-antisymmetric` |
| `-idemp` | Idempotency | `meet-idemp`, `join-idemp` |
| `-monotone` | Monotonicity | `*-monotone` |
| `-unique` | Uniqueness | `ide-unique` |
| `-univ` | Universal property | `-univ` |

#### Apostrophe Variants

An apostrophe (`'`) suffix marks a **variant** or alternative implementation with a different type signature:

- `++` vs `++'`, `toFin` vs `toFin'`, `fromEquiv` vs `fromEquiv'`

```arend
\func \infixr 5 ++ {A : \Type} (xs ys : Array A) : Array A
\func \infixr 5 ++' {A : \Type} (xs : Array A) {n : Nat} (ys : Array A n) : Array A (xs.len Nat.+ n)
```

### 1.6 Single-Letter Identifiers

Single-letter names follow these conventions:

| Letters | Typical use |
|---|---|
| `A`, `B`, `C`, `E`, `J`, `P`, `Q`, `S` | Type parameters (uppercase) |
| `x`, `y`, `z`, `a`, `b`, `c` | Elements of a type/set |
| `n`, `m`, `k` | Natural numbers |
| `i`, `j` | Indices (`Fin n`) |
| `f`, `g`, `h` | Functions |
| `p`, `q`, `r` | Proofs / path equalities |
| `e` | Equivalences or neutral elements (context-dependent) |

**Pattern**: Type parameters use uppercase single letters; value parameters use lowercase.

### 1.7 Operator and Symbolic Names

Operators are defined with `\infixl`, `\infixr`, or `\infix` fixity declarations. When possible, both an ASCII name and a Unicode alias are provided via `\alias`.

**Standard precedence levels:**

| Level | Typical use |
|---|---|
| 0–1 | Logical connectives (`<->`, `/=`) |
| 2 | Equality reasoning (`qed`, `==<`) |
| 4 | Comparisons (`<`, `<=`, `>=`, `>`, `#`) |
| 5 | Concatenation (`::`, `++`) |
| 6–7 | Additive and multiplicative (`+`, `-`, `*`) |
| 8 | Composition (`o`, `∘`) |
| 9 | Path composition (`*>`, `<*`, `<=∘`) |

```arend
\func \infixl 7 * : E -> E -> E
\func \infixr 9 *> {A : \Type} {a a' a'' : A} (p : a = a') (q : a' = a'')
\func \infixr 8 o {A B C : \Type} (g : B -> C) (f : A -> B)
\func \infix 4 <= : E -> E -> \Prop
```

---

## 2. Structural Conventions

### 2.1 `\where` Clauses

`\where` blocks serve three distinct purposes, all of which are legitimate:

**a) Scoped proof helpers** — helpers used only within the enclosing proof:
```arend
\lemma ipow_+ {a : E} {x y : Int} : ipow a (x + y) = ipow a x * ipow a y
  \where {
    \open Arith.Int.IntRing(+, +-comm)
    \lemma ipow_- {a : E} {n m : Nat} : ipow a (n Nat.- m) = pow a n * pow (inverse a) m
  }
```

**b) Namespace groupings** — definitions logically belonging to a type:
```arend
\record MonoidHom ... \where {
  \func equals ...
  \func id ...
  \func presInv ...
}
```

**c) Nested structures** — alternative implementations and sub-proofs:
```arend
\class Monoid \extends Pointed, Semigroup
  \where {
    \protected \func equals {M N : Monoid} (p : M = {\Set} N) ...
      \where {
        \lemma ide-equality : coe (p @) ide right = ide
      }
  }
```

Helper lemmas inside `\where` blocks should be named descriptively. Use `\private` for internal helpers not intended for export; use `\protected` for helpers that should be accessible via qualified names but not opened globally.

### 2.2 `\module` Groupings

Standalone `\module Name \where { ... }` blocks group topically related utilities that do not belong to any specific `\class` or `\record`:

```arend
\module NatOrder \where {
  \data \infix 4 < (n m : Nat) \with ...
  \lemma unsuc< {n m : Nat} (p : suc n < suc m) : n < m
}
\module Sort \where { ... }
```

### 2.3 File-to-Module Naming

Each `.ard` file contains one primary `\class`, `\record`, `\instance`, or `\data` whose name matches the file name. Closely related auxiliary definitions are co-located in the same file. Large auxiliary topics warrant a subdirectory (e.g., `Algebra/Monoid/GCD.ard`, `Algebra/Ring/Ideal.ard`).

- `Monoid.ard` → `\class Monoid`
- `Group.ard` → `\class Group`
- `MonoidHom.ard` → `\record MonoidHom`
- `PartialOrder.ard` → `\class Preorder`, `\class Poset`

### 2.4 Directory Structure

Directories correspond to mathematical domains:

- `Algebra/` — algebraic structures (further subdivided: `Algebra/Ring/`, `Algebra/Group/`, `Algebra/Monoid/`, `Algebra/Domain/`)
- `Order/` — ordered structures
- `Arith/` — concrete arithmetic types (`Nat`, `Int`, `Rat`, `Real`)
- `Data/` — data structures (`List`, `Array`, `Maybe`)
- `Equiv/` — equivalences and homotopy theory
- `Set/` — set-theoretic utilities
- `Logic/` — logic and formal reasoning
- `Topology/`, `Category/`, `Homotopy/`, `AG/` — advanced mathematical areas

### 2.5 Declaration Ordering Within Files

The typical ordering within a file is:

1. `\import` statements (one per line, logically grouped, roughly alphabetical within groups)
2. `\open` statements for frequently used names
3. The primary `\class` / `\record` / `\data` definition
4. Basic operations and constructors
5. Derived classes extending the primary one
6. Properties and lemmas
7. `\instance` declarations
8. Longer helpers in `\where` blocks or separate `\module` blocks

---

## 3. Mathematical Notation Style

### 3.1 `\lemma` vs `\func` vs `\instance`

| Keyword | Use |
|---|---|
| `\lemma` | All proved statements (propositions, equalities, inequalities). Lives in `\Prop`; benefits from proof irrelevance. |
| `\func` | Computational content: constructions, data transformations, type-valued operations. |
| `\instance` | Typeclass instances providing structure witnesses. |
| `\class` / `\record` | Mathematical structures. |

The distinction is strict: a proof of `x = y` is always a `\lemma`; a function producing an element is always a `\func`. The library does not use `\theorem`; all proved statements use `\lemma` regardless of mathematical significance.

### 3.2 Additive vs. Multiplicative Structures

Every multiplicative structure has an additive counterpart formed by prepending `Add` to the class name. Operations rename accordingly:

| Multiplicative | Additive |
|---|---|
| `Monoid` | `AddMonoid` |
| `Group` | `AddGroup` |
| `Semigroup` | `AddSemigroup` |
| `MonoidHom` | `AddMonoidHom` |
| `*` | `+` |
| `ide` | `zro` |
| `inverse` | `negative` |

This pattern is unbroken across the entire library.

### 3.3 Algebraic Hierarchy Naming Patterns

- **Sub-structures** always use the `Sub` prefix: `SubMonoid`, `SubGroup`, `SubSemigroup`, `SubRing`, `SubAddGroup`.
- **Homomorphisms** always use the `Hom` suffix: `MonoidHom`, `AddMonoidHom`, `GroupHom`, `RingHom`, `LinearMap`, `PointedHom`.
- **Opposite structures** are exposed via `\protected \func op` (see §4.5).
- **Commutative variants** use the `C` prefix: `CMonoid` (commutative monoid), `CRing` (commutative ring).

### 3.4 Standard Abbreviations

| Abbreviation | Meaning |
|---|---|
| `ide` | Identity element (multiplicative) |
| `zro` | Zero element (additive) |
| `inv` | Inverse (path inverse in proof context) |
| `distr` | Distributivity |
| `assoc` | Associativity |
| `comm` | Commutativity |
| `func` | Field prefix in a homomorphism record |
| `pmap` | Path map (apply function to a path) |
| `idp` | Identity path |
| `inP` | Constructor of `TruncP` |
| `in~` | Constructor of `Quotient` |
| `LDiv` | Left divisibility |
| `Inv` | Invertibility predicate |
| `Mon` / `CMonoid` | Monoid / commutative monoid |
| `CRing` | Commutative ring |

### 3.5 Unicode vs. ASCII

Unicode is preferred for standard mathematical notation, but every operator that appears in fixity position must also have an ASCII alias via `\alias`. Unicode is used freely for:

- **Order**: `<=`, `<`, `∧`, `∨`, `⊆`, `<=∘`
- **Algebra**: `∘` (composition), `⨯` (product), `⨿` (coproduct)
- **Logic**: `∃`, `∀`, `⊥`
- **Path composition**: `*>`, `<*`

ASCII alternatives (`meet`, `join`, `compose`, `ldistr`) are always available.

```arend
\func <=-transitive \alias \infixr 9 <=∘ {x y z : E} : x <= y -> y <= z -> x <= z
\func Big_meet \alias Big_∧ {n : Nat} (l : Array E (suc n)) : E
\func \fixl 8 o \alias \infixl 8 ∘ {X Y Z : Ob} : Hom Y Z -> Hom X Y -> Hom X Z
```

---

## 4. Definition and Proof Patterns

### 4.1 `func-` Prefix in Homomorphisms

Every field in a homomorphism record that witnesses preservation of structure is prefixed with `func-`:

- `func-ide` — preserves identity
- `func-*` — preserves multiplication
- `func-+` — preserves addition
- `func-BigProd`, `func-BigSum` — preserves big products/sums
- `func-pow` — preserves powers
- `func-LDiv` — preserves left divisibility

### 4.2 `contains_` Prefix in Sub-structures

Fields and lemmas in sub-structure records use `contains_` to name closure conditions:

- `contains_*` — closed under multiplication
- `contains_ide` — contains the identity
- `contains_inverse` — closed under inverses
- `contains_pow` — closed under powers
- `contains_zro`, `contains_negative` — additive variants

### 4.3 Equational Proof Style

Multi-step equational proofs use Arend's `==< ... >==` / `` `qed `` notation, with each step on its own line and the intermediate term displayed explicitly:

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

Short one-step or two-step proofs use inline `*>` (path composition) and `inv` (path reversal):

```arend
pmap (`* a) pow_+ *> *-assoc
```

### 4.4 Pattern Matching with `\elim`

Use explicit `\elim` to specify which arguments are matched:

```arend
\func length {A : \Type} (l : List A) : Nat \elim l
  | nil => 0
  | :: a l => suc (length l)

\func transport2 {A B : \Type} (C : A -> B -> \Type) {a a' : A} {b b' : B} (p : a = a') (q : b = b') (c : C a b) : C a' b' \elim p, q
  | idp, idp => c
```

### 4.5 `op` for Opposite Structures

Every algebraic class with a natural dual provides `\protected \func op` to build the opposite structure by swapping the operation arguments. The `\protected` modifier prevents accidental name clashes when `op` is opened:

```arend
\protected \func op : Monoid E \cowith
  | ide => ide
  | * x y => y * x
  | *-assoc => inv *-assoc
```

This pattern is applied consistently to `Preorder`, `Poset`, `Monoid`, `Group`, `Semiring`, `PseudoRing`, `Precat`, and others.

### 4.6 `from`/`to` Coercions

`\use \coerce` declarations follow the `fromX` / `toX` naming convention:

- `fromX` — "construct this type from X"
- `toX` — "convert to X"

Examples: `fromPointed`, `fromGroup`, `fromMonoid`, `fromRat`, `fromInt`, `fromQEquiv`, `fromEquiv`, `toMonoidHom`, `toFin`, `toProp`.

### 4.7 Symmetry and Variant Patterns

Operations naturally come in symmetric pairs; both halves must always be provided:

- `map` / `map2`, `pmap` / `pmap2` / `pmapd`
- `transport` / `transport2` / `transportInv`
- `index-left` / `index-right`
- `negative_*-left` / `negative_*-right`
- `ret_f` / `f_sec` / `f_ret` (for equivalence/retraction components)

---

## 5. Argument and Type Conventions

### 5.1 Implicit vs. Explicit Arguments

**Implicit `{}`** arguments are used for:
- Universe-polymorphic type parameters that are inferrable: `{A : \Type}`, `{n : Nat}`
- Arguments uniquely determined by later arguments
- Proof/evidence arguments when inference is unambiguous: `{x y z : E}` in `*-assoc`

**Explicit `()`** arguments are used for:
- Primary data the caller must supply
- Functions passed as arguments
- Arguments that cannot be inferred or where inference would be ambiguous

```arend
\func pmap {A B : \Type} (f : A -> B) {a a' : A} (p : a = a') : f a = f a'
\func transport {A : \Type} (B : A -> \Type) {a a' : A} (p : a = a') (b : B a) : B a'
```

### 5.2 Argument Ordering

The standard argument ordering in class fields and function signatures is:

1. Type parameters (implicit `{}`)
2. Structure/class instances (implicit or explicit)
3. Functions or operations (explicit)
4. Primary data (explicit)
5. Proofs and evidence (implicit or explicit, last)

```arend
\func transport {A : \Type} (B : A -> \Type) {a a' : A} (p : a = a') (b : B a) : B a'
--             ^type param  ^function        ^elements   ^proof        ^data
```

In class declarations: carrier type or set first (often inherited via `E`), then operations (infix), then laws (nearly always with implicit arguments).

### 5.3 Universe Levels

| Universe | Meaning |
|---|---|
| `\Type` | General types |
| `\Set` | Sets (types with unique identity proofs) |
| `\Prop` | Propositions (proof-irrelevant types) |
| `\hType n` | Homotopy *n*-types |

Universe polymorphism uses `\plevels` declarations:

```arend
\plevels obj >= hom

\class Precat (Ob : \hType obj) {
  | Hom : Ob -> Ob -> \Set hom
}
```

### 5.4 Special Parameter Annotations

| Annotation | Usage |
|---|---|
| `\property` | Marks proof-relevant parameters: `(\property p : k < n)` |
| `\classifying` | Marks classifying fields in subset classes: `(\classifying contains : S -> \Prop)` |
| `\coerce` | Marks coercion functions in a record: `(\coerce f : A -> B)` |
| `\default` | Provides default implementations of class fields |

### 5.5 `\override` in Record Extensions

Use `\override` in record extensions to specialize the type of an inherited field without re-declaring the carrier:

```arend
\record MonoidHom \extends PointedHom {
  \override Dom : Monoid
  \override Cod : Monoid
  ...
}
```

### 5.6 Visibility Modifiers

| Modifier | Usage |
|---|---|
| `\protected` | Limits visibility; used for `op` (opposite structure) and internal helpers that should be accessible only via qualified names |
| `\private` | Fully internal helpers not intended for export from the `\where` block |

```arend
\protected \func op : Monoid E \cowith ...
\protected \lemma isDefined ...
\private \lemma internalHelper ...
```

### 5.7 `\cowith` vs `\new`

- Use **`\cowith`** when providing a record implementation at the top level of a `\func`, `\instance`, or `\lemma` result.
- Use **`\new`** when constructing a record value as an inline expression.

---

## 6. Documentation and Comment Style

> **Resolved contradiction**: The two source documents diverge significantly on documentation philosophy. The Claude document recommends block-level `{- | ... -}` Haddock-style docstrings for classes/records and `-- |` doc comments for functions and lemmas. The Junie document observes that the library in practice is minimally documented — code is self-documenting through its naming conventions, with comments reserved for major section headings. Both observations reflect real patterns in the codebase: some well-established modules have Haddock comments, but the majority do not. For a **scalable and maintainable math library**, the recommended approach is the following tiered policy: Haddock docstrings on all **public-facing** classes, records, and non-obvious lemmas; section comments for thematic groupings; inline remarks only for genuinely non-obvious steps. Trivial accessor lemmas and obvious definitional equalities do not need documentation.

### 6.1 Block Documentation Comments — `{- | ... -}`

Use `{- | ... -}` (Haddock-style) immediately before public-facing `\class`, `\record`, and `\data` definitions, with no blank line between the comment and the definition:

```arend
{- | Associative ring (not necessarily unital). -}
\class PseudoRing ...

{- | Left ideal of a ring. -}
\record LIdeal ...
```

### 6.2 Line Documentation Comments — `-- |`

Use `-- |` for line-level documentation on non-trivial `\func` and `\lemma` declarations. Reference identifiers with double-backtick syntax ` ``name`` `:

```arend
-- | If ``f : A -> B`` is an equivalence, then ``pmap f`` is also an equivalence.
\func pmapEquiv ...

-- | The intermediate value theorem for strictly monotone functions.
\lemma ivt ...
```

### 6.3 Section Headers

Larger thematic groupings within a file are demarcated with `-- # Section Name`:

```arend
-- # Various operations
\func ...

-- # The order relations
\module NatOrder \where { ... }
```

### 6.4 Inline Remarks

Short informal remarks explaining non-obvious proof steps are placed as `-- comment` on the same line as the step or immediately before a clause. Do not add comments to self-evident steps.

---

## 7. Formatting and Layout Conventions

### 7.1 Indentation

2-space indentation is standard throughout:

- Body of `\class`, `\record`, `\func`, `\lemma`, and `\where` blocks: 2 spaces.
- Nested `\where` blocks: add 2 more spaces per level.

### 7.2 `\import` and `\open` Organization

Imports appear at the top of the file, one per line, in roughly alphabetical order within logical groups (core modules first, specialized ones after). Prefer selective imports to avoid polluting the namespace:

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

Use `\open` at file or `\where` scope to bring frequently used names into scope. When only specific names are needed, use the selective form:

```arend
\open Monoid(LDiv, Inv)
\open AddMonoid
\open Group \hiding (Dec)
```

### 7.3 Pattern Matching Layout

Use **inline patterns** for simple cases:

```arend
\func pred (x : Nat) : Nat
  | zero => 0
  | suc x' => x'
```

Use **multi-line patterns** for complex or multi-argument cases, vertically aligning the `|` bars:

```arend
\func splitAt {A : \Type} (n : Nat) (l : List A) : \Sigma (List A) (List A) \elim n, l
  | 0, l         => (nil, l)
  | suc _, nil   => (nil, nil)
  | suc n, :: a l =>
      \let! (l1, l2) => splitAt n l
      \in (a :: l1, l2)
```

### 7.4 Equational Proof Layout

Align equational chains for readability, with each intermediate term and justification on its own line:

```arend
y                   ==< inv ide-left >==
ide * y             ==< pmap (`* y) (inv inverse-left) >==
(inverse x * x) * y ==< *-assoc >==
inverse x * (x * y) `qed
```

Short proofs use inline composition:

```arend
pmap (`* a) pow_+ *> *-assoc
```

### 7.5 Class and Record Layout

Use compact field definitions with one field per line:

```arend
\class Semigroup \extends BaseSet {
  | \infixl 7 * : E -> E -> E
  | *-assoc {x y z : E} : (x * y) * z = x * (y * z)
}
```

Instance implementations list one field assignment per line:

```arend
\instance ListMonoid {A : \Set} : Monoid (List A)
  | ide => nil
  | * => ++
  | ide-left => idp
  | ide-right => ++_nil
  | *-assoc => ++-assoc
```

### 7.6 Operator Section Syntax

Lambda-section syntax is used for partial application:

- `` `* a `` — right-multiply by `a`
- `` x * __ `` — left-multiply by `x`
- `` `+ b `` — right-add `b`
- `` `*> inv (h a) `` — compose with a path on the right

---

## 8. Quick Reference Summary

### Capitalization Encodes Kind

| Entity kind | Convention | Examples |
|---|---|---|
| Classes / records | PascalCase | `Monoid`, `Ring`, `Preorder`, `MonoidHom` |
| Data types | PascalCase | `List`, `TruncP`, `Empty` |
| Type predicates | PascalCase + `Is` prefix | `IsInj`, `IsSurj`, `IsNilpotent` |
| Instances | PascalCase `<Type><Structure>` | `NatSemiring`, `ListMonoid` |
| Module blocks | PascalCase | `NatOrder`, `Sort` |
| Computational functions | camelCase | `arrayExt`, `headDef`, `mkArray` |
| Algebraic law fields/lemmas | kebab-case | `ide-left`, `*-assoc`, `meet-comm` |
| Operational interaction lemmas | underscore | `pow_+`, `length_++`, `map_id` |
| Data constructors | lowercase | `nil`, `idp`, `yes`, `no` |
| Variables | lowercase single letter | `x`, `n`, `f`, `p` |
| Boolean predicates | camelCase + `is` prefix | `isMono`, `isEpi` |

### Key Rules at a Glance

**Naming**
1. PascalCase for all type-level definitions: classes, records, data, instances, modules.
2. camelCase for computational `\func` definitions.
3. Kebab-case (`-`) for algebraic law fields and positional properties.
4. Underscore (`_`) for operational interaction lemmas; they are not interchangeable with hyphens.
5. `Add` prefix for additive counterparts; `Sub` prefix for sub-structures; `Hom` suffix for homomorphisms.
6. `Is` prefix (PascalCase) for type-level predicates; `is` prefix (camelCase) for boolean predicates.
7. `fromX` / `toX` for coercions; `make` for constructor helpers.
8. `func-` prefix for homomorphism preservation fields; `contains_` for sub-structure closure lemmas.

**Structure**
9. One primary definition per file, matching the filename.
10. `\where` blocks for scoped helpers; `\module` for standalone namespace groupings.
11. `\protected` on `op` and qualified-access helpers; `\private` on fully internal helpers.
12. `\override` in record extensions to specialize inherited field types.
13. Provide both ASCII and Unicode names via `\alias` for fixity operators.

**Proofs**
14. `\lemma` for all propositional content; `\func` for computational content.
15. `==< ... >==` chains for multi-step equational reasoning; `*>` and `inv` for short inline chains.
16. Use `\elim` explicitly for pattern-matching definitions.
17. Follow canonical law-name vocabulary (`*-assoc`, `ide-left`, `ldistr`, etc.) even for new structures.

**Documentation**
18. `{- | ... -}` Haddock comments for public classes, records, and data types.
19. `-- |` line comments for non-trivial functions and lemmas.
20. `-- # Section Name` for major thematic divisions within large files.
21. Rely on naming conventions for self-documentation; avoid over-commenting.

**Formatting**
22. 2-space indentation throughout; nested `\where` blocks add 2 spaces per level.
23. Aligned `==< ... >==` chains with intermediate terms shown explicitly.
24. One import per line, logically grouped and roughly alphabetical.
25. Vertical alignment of `|` bars in multi-case pattern matches.
