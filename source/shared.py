import cadabra2
from cadabra2_defaults import *
__cdbkernel__ = cadabra2.__cdbkernel__

__cdbtmp__ = Coordinate(Ex(r'''{t,x,y,z}'''), Ex(r'''''') )
__cdbtmp__ = Indices(Ex(r'''{a,b,c,d,e,f,i,j,k,l,m,n,o,p,q,r,s,u#}'''), Ex(r'''position=independent,values={t,x,y,z})''') )

__cdbtmp__ = PartialDerivative(Ex(r'''\partial{#}'''), Ex(r'''''') )
__cdbtmp__ = Derivative(Ex(r'''D{#}'''), Ex(r'''''') )
__cdbtmp__ = Derivative(Ex(r'''DBar{#}'''), Ex(r'''''') )
__cdbtmp__ = LaTeXForm(Ex(r'''DBar{#}'''), Ex(r'''"{\bar{D}}")''') )

__cdbtmp__ = Depends(Ex(r'''N'''), Ex(r'''t,x,y,z)''') )

__cdbtmp__ = Symmetric(Ex(r'''g_{a b}'''), Ex(r'''''') )
__cdbtmp__ = Symmetric(Ex(r'''g^{a b}'''), Ex(r'''''') )
__cdbtmp__ = KroneckerDelta(Ex(r'''g_{a}^{b}'''), Ex(r'''''') )
__cdbtmp__ = KroneckerDelta(Ex(r'''g^{a}_{b}'''), Ex(r'''''') )

# g_{a b}::Depends(t,x,y,z).
# g^{a b}::Depends(t,x,y,z).

__cdbtmp__ = Symmetric(Ex(r'''gBar_{a b}'''), Ex(r'''''') )
__cdbtmp__ = Symmetric(Ex(r'''gBar^{a b}'''), Ex(r'''''') )
__cdbtmp__ = KroneckerDelta(Ex(r'''gBar_{a}^{b}'''), Ex(r'''''') )
__cdbtmp__ = KroneckerDelta(Ex(r'''gBar^{a}_{b}'''), Ex(r'''''') )
__cdbtmp__ = LaTeXForm(Ex(r'''gBar{#}'''), Ex(r'''"{\bar{g}}")''') )

# gBar_{a b}::Depends(t,x,y,z).
# gBar^{a b}::Depends(t,x,y,z).

# A_{a b}::Depends(t,x,y,z).
# A^{a b}::Depends(t,x,y,z).

__cdbtmp__ = Depends(Ex(r'''\phi'''), Ex(r'''t,x,y,z)''') )
# detg::Depends(t,x,y,z).
__cdbtmp__ = LaTeXForm(Ex(r'''detg'''), Ex(r'''"{g}")''') )

__cdbtmp__ = Symmetric(Ex(r'''A_{a b}'''), Ex(r'''''') )
__cdbtmp__ = Symmetric(Ex(r'''K_{a b}'''), Ex(r'''''') )
__cdbtmp__ = Symmetric(Ex(r'''R_{a b}'''), Ex(r'''''') )

__cdbtmp__ = Symmetric(Ex(r'''ABar_{a b}'''), Ex(r'''''') )
__cdbtmp__ = Symmetric(Ex(r'''ABar^{a b}'''), Ex(r'''''') )
__cdbtmp__ = LaTeXForm(Ex(r'''ABar{#}'''), Ex(r'''"{\bar{A}}")''') )

__cdbtmp__ = LaTeXForm(Ex(r'''RBar{#}'''), Ex(r'''"{\bar{R}}")''') )

__cdbtmp__ = LaTeXForm(Ex(r'''GammaBar{#}'''), Ex(r'''"{\bar{\Gamma}}")''') )
__cdbtmp__ = TableauSymmetry(Ex(r'''GammaBar^{a}_{b c}'''), Ex(r'''shape={2}, indices={1,2})''') )
__cdbtmp__ = TableauSymmetry(Ex(r'''GammaBar_{a b c}'''), Ex(r'''shape={2}, indices={1,2})''') )

__cdbtmp__ = LaTeXForm(Ex(r'''trK'''), Ex(r'''"{{\rm tr} K}")''') )

dsin  = Ex(r''' \partial_{a?}{\sin(A?)} ->  \cos(A?)\partial_{a?}{A?}'''); _=dsin 
dcos  = Ex(r''' \partial_{a?}{\cos(A?)} -> -\sin(A?)\partial_{a?}{A?}'''); _=dcos 
dexp  = Ex(r''' \partial_{a?}{\exp(A?)} ->  \exp(A?)\partial_{a?}{A?}'''); _=dexp 
dlog  = Ex(r''' \partial_{a?}{\log(A?)} ->    (1/A?)\partial_{a?}{A?}'''); _=dlog 

defG2GBarD  = Ex(r''' g_{a b} -> \exp(4\phi) gBar_{a b}'''); _=defG2GBarD 
defG2GBarU  = Ex(r''' g^{a b} -> \exp(-4\phi) gBar^{a b}'''); _=defG2GBarU 

defGamma  = Ex(r''' \Gamma^{a}_{b c} ->(1/2) g^{a e} (   \partial_{b}{g_{e c}} + \partial_{c}{g_{b e}} - \partial_{e}{g_{b c}})'''); _=defGamma 

defRiem  = Ex(r''' R^{a}_{b c d} ->\partial_{c}{\Gamma^{a}_{b d}} + \Gamma^{a}_{e c} \Gamma^{e}_{b d} - \partial_{d}{\Gamma^{a}_{b c}} - \Gamma^{a}_{e d} \Gamma^{e}_{b c}'''); _=defRiem 

defRab  = Ex(r''' R_{a b} -> R^{c}_{a c b}'''); _=defRab 

# This is my trick to sort product terms, I use it in prefernce to Cadabra's own sort_product
# LCB: fix this -- must move the \partial{foo} ahead of foo
# LCB: really? why?
def product_sort (ex):
    substitute (ex,Ex(r''' N                            -> A001           ''', False))
    substitute (ex,Ex(r''' trK                          -> A002           ''', False))
    substitute (ex,Ex(r''' A_{a b}                      -> A003_{a b}     ''', False))
    substitute (ex,Ex(r''' A^{a b}                      -> A004^{a b}     ''', False))
    substitute (ex,Ex(r''' ABar_{a b}                   -> A005_{a b}     ''', False))
    substitute (ex,Ex(r''' ABar^{a b}                   -> A006^{a b}     ''', False))
    substitute (ex,Ex(r''' g_{a b}                      -> A007_{a b}     ''', False))
    substitute (ex,Ex(r''' g^{a b}                      -> A008^{a b}     ''', False))
    substitute (ex,Ex(r''' gBar_{a b}                   -> A009_{a b}     ''', False))
    substitute (ex,Ex(r''' gBar^{a b}                   -> A010^{a b}     ''', False))
    substitute (ex,Ex(r''' GammaBar^{a}                 -> A011^{a}       ''', False))
    substitute (ex,Ex(r''' GammaBar^{a}_{b c}           -> A012^{a}_{b c} ''', False))
    substitute (ex,Ex(r''' GammaBar_{a b c}             -> A013_{a b c}   ''', False))
    substitute (ex,Ex(r''' \partial_{a}{N}              -> A014_{a}       ''', False))
    substitute (ex,Ex(r''' \partial_{a b}{N}            -> A015_{a b}     ''', False))
    substitute (ex,Ex(r''' \partial_{a}{\phi}           -> A016_{a}       ''', False))
    substitute (ex,Ex(r''' \partial_{a b}{\phi}         -> A017_{a b}     ''', False))
    substitute (ex,Ex(r''' \partial_{a}{GammaBar^{b}}   -> A018_{a}^{b}   ''', False))
    substitute (ex,Ex(r''' \partial_{a}{gBar_{c d}}     -> A019_{a c d}   ''', False))
    substitute (ex,Ex(r''' \partial_{a}{gBar^{c d}}     -> A020_{a}^{c d} ''', False))
    substitute (ex,Ex(r''' \partial_{a b}{gBar_{c d}}   -> A021_{a b c d} ''', False))
    sort_product   (ex)
    rename_dummies (ex)
    substitute (ex,Ex(r''' A001                         -> N                          ''', False))
    substitute (ex,Ex(r''' A002                         -> trK                        ''', False))
    substitute (ex,Ex(r''' A003_{a b}                   -> A_{a b}                    ''', False))
    substitute (ex,Ex(r''' A004^{a b}                   -> A^{a b}                    ''', False))
    substitute (ex,Ex(r''' A005_{a b}                   -> ABar_{a b}                 ''', False))
    substitute (ex,Ex(r''' A006^{a b}                   -> ABar^{a b}                 ''', False))
    substitute (ex,Ex(r''' A007_{a b}                   -> g_{a b}                    ''', False))
    substitute (ex,Ex(r''' A008^{a b}                   -> g^{a b}                    ''', False))
    substitute (ex,Ex(r''' A009_{a b}                   -> gBar_{a b}                 ''', False))
    substitute (ex,Ex(r''' A010^{a b}                   -> gBar^{a b}                 ''', False))
    substitute (ex,Ex(r''' A011^{a}                     -> GammaBar^{a}               ''', False))
    substitute (ex,Ex(r''' A012^{a}_{b c}               -> GammaBar^{a}_{b c}         ''', False))
    substitute (ex,Ex(r''' A013_{a b c}                 -> GammaBar_{a b c}           ''', False))
    substitute (ex,Ex(r''' A014_{a}                     -> \partial_{a}{N}            ''', False))
    substitute (ex,Ex(r''' A015_{a b}                   -> \partial_{a b}{N}          ''', False))
    substitute (ex,Ex(r''' A016_{a}                     -> \partial_{a}{\phi}         ''', False))
    substitute (ex,Ex(r''' A017_{a b}                   -> \partial_{a b}{\phi}       ''', False))
    substitute (ex,Ex(r''' A018_{a}^{b}                 -> \partial_{a}{GammaBar^{b}} ''', False))
    substitute (ex,Ex(r''' A019_{a c d}                 -> \partial_{a}{gBar_{c d}}   ''', False))
    substitute (ex,Ex(r''' A020_{a}^{c d}               -> \partial_{a}{gBar^{c d}}   ''', False))
    substitute (ex,Ex(r''' A021_{a b c d}               -> \partial_{a b}{gBar_{c d}} ''', False))
    return ex
