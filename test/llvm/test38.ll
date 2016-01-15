; ModuleID = '../src/test38.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test38(i32* %value1) #0 {
  %1 = alloca i32*, align 8
  store i32* %value1, i32** %1, align 8
  %2 = load i32** %1, align 8
  store i32 1, i32* %2, align 4
  ret i32 10
}

; Function Attrs: nounwind
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %value1 = alloca i32, align 4
  store i32 0, i32* %1
  %2 = call i32 @test38(i32* %value1)
  ret i32 %2
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
