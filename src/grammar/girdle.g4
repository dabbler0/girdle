grammar girdle;

/* A single first-order logic expression */
primary_fol_expression
    : expression
    | '(' fol_expression ')'
    ;

fol_expression
    : fol_universal_quantifier
    ;

fol_universal_quantifier
    : 'forall' Variable '.' fol_expression
    | fol_existential_quantifier
    ;

fol_existential_quantifier
    : 'exists' Variable '.' fol_expression
    | fol_implication_or_equivalence
    ;

fol_implication_or_equivalence
    : fol_implication
    | fol_equivalence
    ;

fol_implication
    : fol_disjunction '=>' fol_expression
    | fol_disjunction
    ;

fol_equivalence
    : fol_disjunction '<=>' fol_expression
    | fol_disjunction
    ;

fol_disjunction
    : fol_conjunction 'or' fol_disjunction
    | fol_conjunction
    ;

fol_conjunction
    : fol_negation 'and' fol_negation
    | fol_negation
    ;

fol_negation
    : Not primary_fol_expression
    | primary_fol_expression
    ;

expression
    : primary_expression+
    ;

primary_expression
    : Variable
    | '(' expression ')'
    ;

line
    : fol_expression EOF
    ;

Lparen : '(';
Rparen : ')';
Dot : '.';
Not : ('not' | '~');
Forall : 'forall';
Exists : 'exists';
Implies : '=>';
Whitespace
   : (' ' | '\n' | '\t' | '\r') + -> skip
   ;
Variable
    : ~(' ' | '\n' | '\t' | '\r' | '(' | ')' | '.' ) ~(' ' | '\n' | '\t' | '\r' | '(' | ')' | '.' | '=')*
    ;
