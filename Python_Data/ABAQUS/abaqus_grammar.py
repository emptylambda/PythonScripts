abaqus_grammar = r"""
    ?start: list
    ?value: node
          | misc
          | _HEADING
          | element
          | nset
          | nsetgenerate
          | elset
          | elsetgenerate
          | _ENDPART
          | _ENDINSTANCE
          | endstep
          | shellsection
          | instance
          | surface
          | _ENDASSEMBLY

    list: [(_newline value)*]
    _HEADING:"*Heading"
    node:"*Node" _NL [(indexed4fields _NL)*]
    indexed4fields: index "," floatingpoint "," floatingpoint "," floatingpoint


    misc:"*" WORD "," [argument ("," argument)*]
    argument: (WORD "=" (CNAME | FLOAT))

    surface:"*Surface" "," [argument ("," argument)*] _NL [CNAME ("," CNAME)*]

    element:"*Element" [("," argument)*] _NL [(indexed_n_fields _NL)*]
    indexed_n_fields: NUMBER ("," NUMBER)*

    nset:"*Nset" [("," argument)*] _NL listnumber
    nsetgenerate:"*Nset" [("," argument)*] ", generate" _NL listnumber

    listnumber: [([NUMBER ("," NUMBER)*](",")? _NL)+]

    elset:"*Elset" [("," argument)*] _NL listnumber
    elsetgenerate:"*Elset" [("," argument)*] ", generate" _NL NUMBER "," NUMBER "," NUMBER _NL

    shellsection:"*Shell Section" [("," argument)*] [([floatingpoint ("," NUMBER)*] _NL)*]

    instance:"*Instance" [("," argument)*] [([floatingpoint ("," floatingpoint)*] _NL)*]

    endstep: "*End Step"
    _ENDPART: "*End Part"
    _ENDINSTANCE: "*End Instance"
    _ENDASSEMBLY: "*End Assembly"

    CNAME: ("_"|LETTER)("_"|"-"|LETTER|DIGIT)*

    floatingpoint: SIGNED_NUMBER
    index: NUMBER

    %import common.SIGNED_NUMBER
    %import common.LETTER
    %import common.WORD
    %import common.DIGIT
    %import common.NUMBER
    %import common.FLOAT
    %import common.WS_INLINE
    %ignore WS_INLINE
    %ignore ", internal"

    _NL: /(\r?\n[\t ]*)+/
    _EVERYTHING: /.+/
    _COMMENT: DOUBLESTAR/[^\n]*/
    DOUBLESTAR: "**"
    _newline: (_NL | _COMMENT )*
"""
