# Generated from f://STUDY MATERIAL//HK232//NGUYEN LY NNLT//ASSIGNMENT//BTL-Extra//initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#mptype.
    def enterMptype(self, ctx:ZCodeParser.MptypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#mptype.
    def exitMptype(self, ctx:ZCodeParser.MptypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body.
    def enterBody(self, ctx:ZCodeParser.BodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body.
    def exitBody(self, ctx:ZCodeParser.BodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp.
    def enterExp(self, ctx:ZCodeParser.ExpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exp.
    def exitExp(self, ctx:ZCodeParser.ExpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcall.
    def enterFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcall.
    def exitFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass



del ZCodeParser